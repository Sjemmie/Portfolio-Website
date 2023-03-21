import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE date='2088.10.14'")
result = cursor.fetchall()
print(result)

# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.14'")
result = cursor.fetchall()
print(result)

# Insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()