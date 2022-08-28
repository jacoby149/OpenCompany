import pymongo
from bson.objectid import ObjectId
import app.settings as settings
import app.models as models
import app.web10records as records
import app.exceptions as exceptions
import os
import re
import datetime


#################################
####### CONNECTING TO DB ########
#################################

client_url = os.environ.get("DB_URL")
if not client_url:
    DB_URL = settings.DB_URL
client = pymongo.MongoClient(DB_URL)
db = client[settings.DB]


################################
######### User Data ############
################################

def get_user(username):
    user_collection = db['users']
    return user_collection.find_one({"login": username})

def insert_user(user_data):
    db['users'].insert_one(user_data)

def promote_user(filter,update):
    db["users"].update_one(filter,update)