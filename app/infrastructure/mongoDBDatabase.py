from dotenv import load_dotenv

import os
from pymongo import MongoClient

load_dotenv()

# DB
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PWD = os.environ.get('MONGO_PWD')
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

def get_mongo_client():
    try:
        mongo_client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/')
        print("------- * D B c o n n e c t s u c c e s s * -------")
        return mongo_client
    
    except Exception as e:
        print('DB connection Error',e)
        
def get_collection(mongo_client, db_name='test', collection_name='tests'):
    try:
        db = mongo_client[db_name]
        client = db[collection_name]
        print("------- * G e t c o l l e c t i o n s u c c e s s * -------")
        return client
    
    except Exception as e:
        print('Get collection Error',e)
        
mongoDB_connection_pool = get_collection(get_mongo_client())
