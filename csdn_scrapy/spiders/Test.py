import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.csdn_db
collection = db.csdn_info
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

count = collection.find({'uid':'u010979642'}).count()
print(count)
# if(results.size>0):
#     print("has exists")

