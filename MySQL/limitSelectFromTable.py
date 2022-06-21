import mysql.connector

dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

dbCursor = dbConn.cursor()

#LIMITING RESULTS TO ONLY FIVE
dbCursor.execute("SELECT * FROM users LIMIT 5")

print(dbCursor.fetchall())

#start from position 3 and limit results to 5
dbCursor.execute("SELECT * FROM users LIMIT 5 OFFSET 2")

print(dbCursor.fetchall())