import bcrypt
from datetime import datetime, date



def serialize_object_id(document):
    document['_id'] = str(document['_id'])
    return document

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def prepare_user_data(user_data):
    if isinstance(user_data.get("date_of_birth"), date):
        user_data["date_of_birth"] = datetime.combine(user_data["date_of_birth"], datetime.min.time())
    user_data["state"] = "active"
    return user_data