"""
Created by Modester Vihambwa
"""
import os
import sqlite3

# connect to database
conn = sqlite3.connect('vehicle.db')

# Create cursor
cur = conn.cursor()

# Check if table exists
#cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='toll'")
# if cur.fetchone()[0] == 1:
#   while cur.fetchone()[0] == 1:
#       cur.execute("SELECT * FROM toll ")
# else:
#create table for toll collection
cur.execute("CREATE TABLE toll (vehicle_id text, descr int, acc_balance int)")

vehicles = [
    ('97 8F 0B 3C', 'KCA987C', '2100'),
    ('C7 C8 8D 3F', 'KAD542K', '3200'),
    ('A3 4B 7E A3', 'KDB768F', '50'),
]

# INSERT DATA TO DATABASE
#cur.executemany('INSERT INTO toll VALUES (?,?,?)', vehicles)

rfid = 'A3 4B 7E A3'
cur.execute("SELECT * FROM toll WHERE vehicle_id = ?", (rfid,))
print(cur.fetchall())

# commit changes to database
conn.commit()

# Close database connection
conn.close()


new_acc = arduino.readline().decode().strip()

    if new_acc == "100":
        print(new_acc)

    val = 100
    val1 = str(val)