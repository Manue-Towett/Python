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

#create table named users
dbCursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")