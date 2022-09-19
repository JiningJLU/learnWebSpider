import pymongo

MONGO_CONNECTION = 'mongodb://localhost:27017/'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


def save_data(data):
    # 参数一 查询条件 参数二 指定要更新，并且给出更新的数据 参数三 upsert=True 如果没有找到匹配的数据，就插入一条新的数据
    collection.update_one({
        'name': data.get('name')
    },{
        '$set': data
    }, upsert=True)