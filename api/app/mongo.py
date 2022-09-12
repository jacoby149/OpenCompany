import pymongo
import app.settings as settings
import os
import datetime as dt


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

def promote_user(user,mentor):
    db["promotions"].insert_one(
        {
            "user":user["node_id"],
            "mentor":mentor["node_id"],
            "former_rank":user["rank"],
            "promotion_rank":user["rank"]+1,
            'dt': dt.datetime.now().isoformat()
        })
    db["users"].update_one({"node_id":user["node_id"]},{ "$inc": { "rank": 1}})