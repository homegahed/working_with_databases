import sqlite3 
print('sqlite3 library is imported')
print('=' * 20)


connection = sqlite3.connect('movies.db')
print('connection to databses')
print('=' * 20)


cursor = connection.cursor()
print('Create a cursor to execute commands and queries on the database')
print('=' * 20)



# #cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")
# print('Inserting our first entry to Movies tables of movies database')
# print('=' * 20)


# cursor.execute("select * from movies")
# print('Retrieving data from movies database (fetching data)')
# print('=' * 20)




# print(f'printing the data retrieved from DD \n {cursor.fetchone()}')




# famousfilms = [ ('Pulp Fiction', 'Quentin Tarantino', 1994),
# 				('Back to the Future', 'Steven Spielberg', 1985),
# 				('Moonrise Kingdom', 'Wes Anderson', 2012) ]


# cursor.executemany("INSERT INTO Movies VALUES (?, ?, ?)", famousfilms)
# print('Inserting bulk data')
# print('=' * 20)

# records = cursor.execute("SELECT * FROM Movies")

#print(cursor.fetchall())
#print('Retrieving & fetching all data with fetchall()')
#print('=' * 20)




# for record in records:
# 	print(record)
# print('Retrieving & fetching all data with for loop')
# print('=' * 20)





release_year = (1985, )

cursor.execute('SELECT * FROM Movies WHERE year=?', release_year)
print(cursor.fetchall())
print('Filtering table and retrieve filtered data')
print('=' * 20)




connection.commit()
print('Commit the changes to the database')
print('=' * 20)


connection.close()
print('Saving changes and closing the connection to the database')
print('=' * 20)