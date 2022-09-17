import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['test']

collection = db['students']

# 更新数据
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 删除数据
result = collection.delete_one(condition)
print(result)
print(result.deleted_count)

result = collection.delete_many({'age': {'$lt': 25}})
print(result)
print(result.deleted_count)