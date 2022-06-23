import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

shopDB = myClient["shop"]

customersTable = shopDB["customers"]

#check if table exists
print(shopDB.list_collection_names())

#delete collection
customersTable.drop()

#check if table still exists
print(shopDB.list_collection_names())