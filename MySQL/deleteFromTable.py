import mysql.connector

dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

dbCursor = dbConn.cursor()

dbCursor.execute("DELETE FROM users WHERE address = 'Kahawa wendani'")

dbCursor.execute("SELECT * FROM users")

print(dbCursor.fetchall())

#preventing sql injections by using %s
address = ('Githurai',)
dbCursor.execute("DELETE FROM users WHERE address = %s", address)

dbCursor.execute("SELECT * FROM users")

print(dbCursor.fetchall())

#commit changes to database
dbConn.commit()