from fastapi import APIRouter, Depends
from app.services.auth import  get_admin_user
import logging
from threading import Thread
from db import get_users_collection


users_collection = get_users_collection()

router = APIRouter()

@router.get("/process-users/", dependencies=[Depends(get_admin_user)])
async def process_users():
    #batch processing
    average_temperature = process_all_users()
    
    if average_temperature is not None:
        return {"average_temperature": average_temperature}
    return {"message": "No valid weather data available."}

# logging
logging.basicConfig(level=logging.INFO)

#function to group users by city
def group_users_by_location(users):
    location_groups = {}
    for user in users:
        city = user.get('city')
        if city:
            if city not in location_groups:
                location_groups[city] = []
            location_groups[city].append(user)
        else:
            logging.warning(f"Missing city for user {user['_id']}. Excluding from calculation.")
    return location_groups


def process_user_chunk(user_chunk):
    total_temperature = 0
    valid_user_count = 0
    for user in user_chunk:
        weather = user.get('weather')
        
        # exclude users with missing or invalid weather data
        if weather:
            total_temperature += weather.get('temperature', 0)
            valid_user_count += 1
        else:
            logging.warning(f"Missing weather data for user {user['_id']} in city {user.get('city')}. Excluding from calculation.")
    
    return total_temperature, valid_user_count

# calculate avg temprature
def calculate_average_temperature(results):
    total_temperature = 0
    valid_user_count = 0
    for result in results:
        total_temperature += result[0]
        valid_user_count += result[1]

    if valid_user_count > 0:
        return total_temperature / valid_user_count
    return None

def batch_process_users_by_location(location_groups):
    threads = []
    results = []
    
    def worker(city, user_chunk):
        result = process_user_chunk(user_chunk)
        logging.info(f"Processed {len(user_chunk)} users from {city}")
        results.append(result)

    # thread for each city/location group
    for city, user_chunk in location_groups.items():
        thread = Thread(target=worker, args=(city, user_chunk))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

# fetch users and process them by location
def process_all_users():
    users = list(users_collection.find())
    
    # group users by city
    location_groups = group_users_by_location(users)
    
    # rocess user groups by city in multiple threads
    results = batch_process_users_by_location(location_groups)
    
    # calculate avg temperature
    return calculate_average_temperature(results)
