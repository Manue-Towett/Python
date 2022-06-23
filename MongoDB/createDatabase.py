import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

#Database creating
myDB =myClient['shop']

#Database does not exists yet until collection and document are created
print(myClient.list_database_names())

#check a specific database by name
dbList = myClient.list_database_names()

if 'shop' in dbList:
    print('Database exists')