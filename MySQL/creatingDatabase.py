import mysql.connector

#connecting to mysql server
dbConn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="towett"
)

#creating a cursor
dbCursor = dbConn.cursor()

#creating a database
dbCursor.execute("CREATE DATABASE testDB")

#check if database exists
dbCursor.execute("SHOW DATABASES")

for database in dbCursor:
  print(database)