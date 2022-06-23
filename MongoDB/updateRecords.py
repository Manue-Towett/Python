import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

shopDB =  myClient['shop']

customersTable = shopDB['customers']

#define the value as is in db and the new value
record = {"address":"Khawa sukari"}
newRecord = {"$set":{"address":"Ruiru east"}}

#update record
customersTable.update_one(record, newRecord)

#check the records to see the change
for record in customersTable.find():
    print(record)

#update many records
record = {"address":{"$regex":"^K"}}
newRecord = {"$set":{"address":"Juja"}}

customersTable.update_many(record, newRecord)

for record in customersTable.find():
    print(record)