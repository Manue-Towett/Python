import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

shopDB = myClient["shop"]

customersTable = shopDB["customers"]

#limit search results to two
for record in customersTable.find().limit(2):
    print(record)