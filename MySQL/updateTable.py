import mysql.connector

dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

dbCursor = dbConn.cursor()

#update address in the table users
dbCursor.execute("UPDATE users SET address = 'Githurai' WHERE address = 'Kahawa Sukari'")

#prevent sql injections
address = ("Bomet",)
dbCursor.execute("UPDATE users SET address = 'Kahawa' WHERE address = %s", address)

dbCursor.execute("SELECT * FROM users")

print(dbCursor.fetchall())

dbConn.commit()