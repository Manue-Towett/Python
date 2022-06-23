import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myShop = myClient["shop"]

customersTable = myShop["customers"]

query = {"name":"Towett"}

#delete one record
customersTable.delete_one(query)

#delete many records using regex
query = {"name":{"$regex":"^T"}}

customersTable.delete_many(query)

#check the remaining records
for record in customersTable.find():
    print(record)

#delete all the records
customersTable.delete_many({})

#check whether there are any records
for record in customersTable.find():
    print(record)