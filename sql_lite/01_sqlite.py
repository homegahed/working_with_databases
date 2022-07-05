import sqlite3 
print('sqlite3 library is imported')
print('=' * 20)




connection = sqlite3.connect('movies.db')
print('connection is made')
print('=' * 20)

cursor = connection.cursor()
print('Create a cursor to execute commands and queries on the database')
print('=' * 20)


cursor.execute( ''' CREATE TABLE IF NOT EXISTS Movies (Tile TEXT, Director TEXT, Year INT)''')
print('Creating "Movies" table')
print('=' * 20)


connection.commit()
print('Commit the changes to the database')
print('=' * 20)


connection.close()
print('Saving changes and closing the connection to the database')
print('=' * 20)