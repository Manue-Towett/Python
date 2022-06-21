import mysql.connector

#create connection
dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB" 
)

#create cursor
dbCursor =  dbConn.cursor()

#define sql statement for inserting values
sql = "INSERT INTO users (name, address) VALUES (%s,%s)"

#store values to be inserted into database in a list
data = [
    ('Emmanuel', 'Kahawa wendani'),
    ('Towett', 'Kahawa Sukari'),
    ('Kipngetich', 'Githurai'),
    ('Modester', 'Ruai'),
    ('Maxwell', 'Bomet')
]

#insert a value in the data list to the table
dbCursor.execute(sql,data[0])

#insert all the values in the list into the database
dbCursor.executemany(sql, data)

#commit changes to database
dbConn.commit()

#check number of rows being inserted into database
rowsInDB = dbCursor.rowcount

print(rowsInDB)

#return the id of the inserted values
rowID = dbCursor.lastrowid

print(rowID)