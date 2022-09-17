import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['test']

collection = db['students']

result = collection.find_one({'name': 'Mike'})

print(type(result))
print(result)

result = collection.find_one({
    '_id': ObjectId('63257c6891f8e80a2635074e')
})

print(result)

results = collection.find({
    'age': 20
})

# 类型是pymongo.cursor.Cursor类型
print(results)
for result in results:
    print(result)

results = collection.find({
    'age': {
        '$gt': 20
    }
})
for result in results:
    print(result)

results = collection.find({
    'name': {
        '$regex': '^M.*?'
    }
})

# 书上写的方法过时了，要这么统计才行
count = collection.count_documents({'age': 20})
print(count)

sorted_results = collection.find({'age': 20}).sort('name', pymongo.ASCENDING)
for sorted_result in sorted_results:
    print(sorted_result)

sorted_results = collection.find({'age': 20}).sort('name', pymongo.ASCENDING).skip(1)
print("Skipped: ")
for sorted_result in sorted_results:
    print(sorted_result)

sorted_results = collection.find({'age': 20}).sort('name', pymongo.ASCENDING).skip(1)
print("limit: ")
for sorted_result in sorted_results:
    print(sorted_result)