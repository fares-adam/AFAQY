import logging
from app.services.weather import fetch_weather_data
from pymongo import MongoClient
from db import get_users_collection

users_collection = get_users_collection()

async def start_weather_updater():
    try:
        
        users = users_collection.find()
        for user in users:
            try:
                weather = await fetch_weather_data(user['city'])
                if weather:
                    users_collection.update_one({"_id": user["_id"]}, {"$set": {"weather": weather}})
                    logging.info(f"weather update successfull for user : {user['_id']}")
                else:
                    logging.warning(f"Failed to fetch weather for user: {user['_id']}")
            except Exception as e:
                    logging.error(f"Error occurred while fetching weather for user {user['_id']}: {e}")
    except Exception as e:
        logging.error(f"Failed to fetch users from MongoDB: {e}")
