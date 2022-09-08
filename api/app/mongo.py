import pymongo
import app.settings as settings
import os

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

def get_user(node_id):
    user_collection = db['users']
    return user_collection.find_one({"node_id": node_id})

def init_user(gh_data):
    user_data = {"rank":0}
    user_data.update(gh_data)
    insert_user(user_data)

def insert_user(user_data):
    db['users'].insert_one(user_data)

def promote_user(filter,update):
    db["users"].update_one(filter,update)