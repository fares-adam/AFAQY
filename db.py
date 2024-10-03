from pymongo import MongoClient

# create a MongoDB client
client = MongoClient("mongodb://localhost:27017/")

# connect to db
db = client['user_db']

#'users' collection
users_collection = db['users']

def get_users_collection():
    return users_collection