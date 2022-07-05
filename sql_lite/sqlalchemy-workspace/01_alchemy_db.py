# importing sqlalchemy library
import sqlalchemy as db


# connecting to the database with SQLAlchemy create_engine
engine = db.create_engine('sqlite:///movies.db')


# creating a connection with SQLAlchemy engine
connection = engine.connect()


# Retrieve database metadata
metadata = db.MetaData()


# Retrieve table from database
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# Querying database table with SQLAlchemy
query = db.select([movies])

# Executing the queries
result_proxy = connection.execute(query)

# Fetching data from result_proxy
result_set = result_proxy.fetchall()

print('=' * 20)
print(result_set[0])
print('=' * 20)
print(result_set[1:3])
print('=' * 20)


# Querying and filtering with SQLAlchemy
query2 = db.select([movies]).where(movies.columns.Director == 'Martin Scorsese')
result_proxy2 = connection.execute(query2)
result_set2 = result_proxy2.fetchall()

print('-' * 20)
print(result_set2)
print('-' * 20)
print(result_set2[0])
print('-' * 20)


# Inserting new records with SQLAlchemy
query3 = movies.insert().values(Tile="Psycho", 
								Director="Alfred Hitchcock", Year=1960)

# Executing the queries
connection.execute(query3)




# Querying database table with SQLAlchemy
query4 = db.select([movies])

# Executing the queries
result_proxy4 = connection.execute(query4)

# Fetching data from result_proxy
result_set4 = result_proxy4.fetchall()


print('*' * 20)
print(result_set4)
print('*' * 20)

#print(movies.columns)

print('Completed')