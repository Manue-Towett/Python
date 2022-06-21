import mysql.connector

dbConn =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

dbCursor = dbConn.cursor()

#delete table
dbCursor.execute("DROP TABLE customers")

#check tables in database
dbCursor.execute("SHOW TABLES")

print(dbCursor.fetchall())

#delete table if it exists
dbCursor.execute("DROP TABLE IF EXISTS customers")