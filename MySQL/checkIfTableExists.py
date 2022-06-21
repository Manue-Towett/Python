import mysql.connector

#create connection
dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

#create cursor
dbCursor = dbConn.cursor()

#check if table exists
dbCursor.execute("SHOW TABLES")

for table in dbCursor:
    print(table)