import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')

shopDB = myClient['shop']

#creating a collection
customersTable = shopDB['customers']

#checking if a collection exists
print(shopDB.list_collection_names())

#check if database exists
print(myClient.list_database_names())

'''
Both the database and the collection do not yet exist until a document is created
'''