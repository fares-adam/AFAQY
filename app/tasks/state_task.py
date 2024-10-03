from datetime import datetime, timedelta
import logging
from db import get_users_collection

users_collection = get_users_collection()
def start_state_updater():
    cutoff = datetime.now() - timedelta(days=30)
    users = users_collection.find({"last_logged_in": {"$lt": cutoff}})
    for user in users:
        if user["state"] == "active":
        # deactivate users who haven't logged in for 30 days
            users_collection.update_one({"_id": user["_id"]}, {"$set": {"state": "inactive"}})
            logging.info(f"User {user['_id']} has been set to Inactive due to inactivity")
