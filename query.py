import sqlite3

conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query = 'select name,population from facts where (population != "None") order by population asc'
cursor.execute(query)
print(cursor.fetchmany(10))