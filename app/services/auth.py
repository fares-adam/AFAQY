from datetime import datetime, timedelta
import bcrypt
import jwt
from pydantic import SecretStr
from app.models.user import User
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from db import get_users_collection

users_collection = get_users_collection()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"

def verify_password(stored_password: str, input_password) -> bool:
    # if input_password is a secretstr
    if isinstance(input_password, SecretStr):
        input_password_str = input_password.get_secret_value()
    else:
        input_password_str = input_password  # if it's already a plain string, use it as is

    #compare
    return stored_password._secret_value == input_password_str

# generate JWT
def generate_jwt(user: User) -> str:
    payload = {
        "sub": user.email,  # Subject: user email
        "role": user.role,  # User role
        "exp": datetime.utcnow() + timedelta(hours=5)  # Expiration in 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def authenticate_user(email: str, password: str):
    user_dict = users_collection.find_one({"email": email})

    if user_dict:
        #dict to user model
        if bcrypt.checkpw(password.encode('utf-8'), user_dict["password"]):
            user_dict["_id"] = str(user_dict["_id"])
            user = User(**user_dict)
        

        # update last log in , state
            users_collection.update_one(
                        {"email": email},  # Find user by email
                        {"$set": {
                        "last_logged_in": datetime.utcnow(),
                        "state": "active"
                        }}
                    )
            # password matched, generate JWT
            token = generate_jwt(user)
            return {"token": token, "user": user}
        else:
            return None
    else:
        return None

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_admin_user(token: str = Depends(oauth2_scheme)):
    user = get_current_user(token)
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return user
