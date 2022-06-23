import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')

shopDB = myClient['shop']

customersTable = shopDB['customers']

#create a document
customersDict = {
    "name":'Towett',
    "address":"Kahawa 34"
}

#insert one record to collection from the dictionary
insertRecord = customersTable.insert_one(customersDict)

#check if table exists
print(shopDB.list_collection_names())

#collection now exists after creating a document

#check inserted id
print(insertRecord.inserted_id)

#mongoDB automatically assigns id to every record which are unique

#inserting a record with a predefined id
customersDict = {
    "name":'Towett',
    "address":"Kahawa 34"
}

insertRecord = customersTable.insert_one(customersDict)

print(insertRecord.inserted_id)

#inserting many documents
customersDict = [
    {"name":"Emmanuel", "address":"Kahawa wendani"},
    {"name":"Kipngetich", "address": "Khawa sukari"},
    {"name":"Modester","address":"Kahawa west"}
]

insertRecords = customersTable.insert_many(customersDict)

print(insertRecords.inserted_ids)