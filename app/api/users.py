
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from app.models.user import User
from app.services.auth import get_current_user, get_admin_user
from bson.objectid import ObjectId
from app.services.weather import fetch_weather_data
from db import get_users_collection
from utils import serialize_object_id, hash_password , prepare_user_data
users_collection = get_users_collection()

router = APIRouter()




# create user
@router.post("/users")
async def create_user(user: User):
    # validate and fetch weather data
    weather = await fetch_weather_data(user.city)
    user_data = user.model_dump()
    user_data["weather"] = weather
    hashed_password = hash_password(user.password.get_secret_value())
    user_data["password"]=hashed_password
    user_data = prepare_user_data(user_data)
    users_collection.insert_one(user_data)
    return {"msg": "User created successfully", "user": serialize_object_id(user_data)}

async def get_user(id: str):
    user = users_collection.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_object_id(user)

@router.get("/users", response_model=List[User])
def get_all_users(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), current_user: dict = Depends(get_admin_user)):
    """
    Fetch all users with pagination.
    Only admins can access this endpoint.
    """
    # fetch all users with pagination (skip/limit)
    users_cursor = users_collection.find({}).skip(skip).limit(limit)
    users = list(users_cursor)

    for user in users:
        user = serialize_object_id(user)

    return users

# update user
@router.put("/users/{id}", dependencies=[Depends(get_current_user)])
async def update_user(id: str, user: User):
    # convert the string id to ObjectId
    try:
        user_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    # convert the pydantic model to dict , remove unset fields
    updated_data = user.model_dump(exclude_unset=True)

    # check if the user exists
    existing_user = users_collection.find_one({"_id": user_id})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # update
    result = users_collection.update_one({"_id": user_id}, {"$set": updated_data})


    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"msg": "User updated successfully"}

# delete user (admin only)
@router.delete("/users/{id}", dependencies=[Depends(get_admin_user)])
async def delete_user(id: str):
    try:
        # convert the string id to ObjectId
        user_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    existing_user = users_collection.find_one({"_id": user_id})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # delete 
    result = users_collection.delete_one({"_id": user_id})

    # raise error if delete failed
    if result.deleted_count == 0:
        raise HTTPException(status_code=500, detail="Failed to delete user")

    return {"msg": "User deleted successfully"}

@router.put("/users/{id}/suspend", dependencies=[Depends(get_admin_user)])
async def suspend_user(id: str):
    try:
    
        user_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    
    existing_user = users_collection.find_one({"_id": user_id})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    #suspend
    result = users_collection.update_one({"_id": user_id}, {"$set": {"state": "suspended"}})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=500, detail="Failed to suspend user")

    return {"msg": "User suspended successfully"}
