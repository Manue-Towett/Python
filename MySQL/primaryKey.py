import mysql.connector

#create connection
dbConn = mysql.connector.connect(
    host = "localhost",
    password = "towett",
    user = "root",
    database = "testDB"
)

#create cursor
dbCursor = dbConn.cursor()

#creating table with a primary key
dbCursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Add primary key to an existing table
dbCursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")