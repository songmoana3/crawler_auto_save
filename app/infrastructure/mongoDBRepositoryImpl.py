from infrastructure import mongoDBDatabase

def mongo_find(query):
    try:
        return mongoDBDatabase.mongoDB_connection_pool.find(*query) 
    except:
        raise "----- * mongoDB find error * -----"