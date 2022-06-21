import mysql.connector

dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

dbCursor = dbConn.cursor()

#select everything from table
dbCursor.execute("SELECT * FROM users")

#fetch only one row
dataFromDB = dbCursor.fetchone()

print(dataFromDB)

#fetch all rows
dataFromDB = dbCursor.fetchall()

#iterate over the result
for record in dataFromDB:
    print(record)

#fetch only name and address columns
dbCursor.execute("SELECT name, address FROM users")

records = dbCursor.fetchall()

for record in records:
    print(record)

#using the where clause to select
dbCursor.execute("SELECT * FROM users WHERE id = 15")

print(dbCursor.fetchone())

#You can also select the records that starts, includes, or ends with a given letter or phrase.
dbCursor.execute("SELECT * FROM users WHERE address LIKE '%Kahawa%'")

print(dbCursor.fetchall())

#to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database, use %s
sql = "SELECT * FROM users WHERE address = %s"
address = ('Kahawa Sukari',)

dbCursor.execute(sql,address)

print(dbCursor.fetchall())

#sorting the result in ascending order alphabetically
dbCursor.execute("SELECT * FROM users ORDER BY name")

print(dbCursor.fetchall())

#sorting the result in descending order
dbCursor.execute("SELECT * FROM users ORDER BY name DESC")

print(dbCursor.fetchall())