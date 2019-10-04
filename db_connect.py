import pyodbc
# In this file we'll make our connection

# Parameters/variables for connection:
server = 'localhost,1433'
database = 'Book_Store'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_rdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)

# Create a cursor
# Allows us to execute read only queries on the db
cursor = conn_rdb.cursor()

