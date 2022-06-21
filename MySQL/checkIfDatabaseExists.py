import mysql.connector

#create connection
#one way of checking if db exists is to put its name inside the connect object when creating connection
dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB" #returns an error if the database doesn't exist
)

#Another way is to create a cursor and use it to check if db exist
#creating a cursor
dbCursor = dbConn.cursor()

#check if database exists
dbCursor.execute("SHOW DATABASES")

for database in dbCursor:
  print(database)