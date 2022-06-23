import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

shopDB = myClient["shop"]

customersTable = shopDB['customers']

#finding the first record in table
findRecord = customersTable.find_one()

print(findRecord)

#finding all the records in table
for record in customersTable.find():
    print(record)

#exclude one column from the result
for record in customersTable.find({},{"_id":0}):
    print(record)