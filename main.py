from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from pymongo import ASCENDING
from app.api import users, admin
from fastapi.security import OAuth2PasswordBearer
from app.services.auth import authenticate_user
from logging_config import setup_logging
from app.tasks.weather_task import start_weather_updater
from app.tasks.state_task import start_state_updater
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db import get_users_collection
from utils import hash_password
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# setup logging
setup_logging()

#api routers
app.include_router(users.router)
app.include_router(admin.router)

scheduler = AsyncIOScheduler()
scheduler.add_job(start_weather_updater, "interval", minutes=60)
scheduler.add_job(start_state_updater, "interval", minutes=1)
scheduler.start()



def create_unique_indexes():
    collection = get_users_collection()

    # create unique index for 'email'
    collection.create_index([("email", ASCENDING)], unique=True)
    # create unique index for 'phone'
    collection.create_index([("phone", ASCENDING)], unique=True)
    print("Unique indexes for 'email' and 'phone' created!")

def indexes_and_admin():
    create_unique_indexes()
    add_admin_user()
    
# register the startup event using add_event_handler
app.add_event_handler("startup", indexes_and_admin)


def add_admin_user():
    
    #  admin user data
    admin_user_data = {
    "name": "admin",             
    "email": "admin@example.com",     
    "date_of_birth": "1990-09-09",                        
    "password": "admin",
    "phone": "07775000" ,
    "city": "Alexandria",
    "state": "active",               
    "last_logged_in": datetime.now(),
    "weather": {},                    
    "role": "admin"                  
}

    # hash password
    admin_user_data["password"] = hash_password(admin_user_data["password"])
    collection = get_users_collection()
    # insert
    existing_user = collection.find_one({"email": admin_user_data["email"]})
    if  not existing_user:
        result = collection.insert_one(admin_user_data)
        print(f"Admin user created with id: {result.inserted_id}")
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str
    
    
# JWT-based Authentication
@app.post("/login")
async def login(creds: LoginRequest):
    user = authenticate_user(creds.email, creds.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": user["token"], "token_type": "bearer"}

