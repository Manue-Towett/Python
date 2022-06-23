import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

shopDB = myClient["shop"]

customersTable = shopDB["customers"]

#sort in ascending order
records = customersTable.find().sort("name")

for record in records:
    print(record)

#sort in descending order
records = customersTable.find().sort("name",-1)

for record in records:
    print(record)