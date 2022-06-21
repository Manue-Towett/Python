import mysql.connector

dbConn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "towett",
    database = "testDB"
)

dbCursor = dbConn.cursor()

#dbCursor.execute("DROP TABLE products")
#create a new table products
dbCursor.execute("CREATE TABLE products (name VARCHAR(255), seller VARCHAR(255), id INT AUTO_INCREMENT PRIMARY KEY)")

#create a list of products to be inserted into database
fruits = [
    ('apple','rc'), 
    ('mango','gh'), 
    ('banana','gy'),
    ('orange','rs'),
    ('pineapple','ty'),
    ('plums','op'),
    ('strawberries','pt')
]

#insert the fruits in the products table
dbCursor.executemany("INSERT INTO products (name,seller) VALUES (%s,%s)",fruits)

#query records in database
dbCursor.execute("SELECT * FROM products")

print(dbCursor.fetchall())

dbConn.commit()

#join products and users
sql = "SELECT users.name AS user, products.name AS fruit FROM users JOIN products ON users.id = products.id"

dbCursor.execute(sql)

print(dbCursor.fetchall())