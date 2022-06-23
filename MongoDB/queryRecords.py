import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

shopDB = myClient["shop"]

customersTable = shopDB["customers"]

query = {"address":"Kahawa wendani"}

#find record containing kahawa wendani in the address
for record in customersTable.find(query):
    print(record)

#filter where the name starts with "M" or higher alphabetically
query = {"name":{"$gt":"M"}}

for record in customersTable.find(query):
    print(record)

#filtering regular expressions
#find name starting with m
query = {"name":{"$regex":"T"}}

for record in customersTable.find(query):
    print(record)