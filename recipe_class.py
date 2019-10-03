import cursor as cursor
import pyodbc

server = 'localhost,1433'
database = 'recipes_db'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_recipes_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)

# Create a cursor
# Allows us to execute read only queries on the db
# Define a class recipe

class RecipeMcServer:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_recipes_db = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_recipes_db.cursor()

    cursor = conn_recipes_db()

    def __filter_query(self, query):
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.__filter_query(query).execute(query)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

# new()
    # create a recipe object
    def create_recipe(self, recipe_id, recipe_name, ingredients, describe_recipe, instructions, postcode):
        self.cursor(f"INSERT INTO recipes (recipe_id, recipe_name, ingredients, describe_recipe, instructions, postcode) VALUES ({recipe_id}, {recipe_name}, {ingredients}, {describe_recipe}, {instructions}, {postcode})"))
        conn_recipes_db.commit()

# save()
    # saves a recipe object to the DB (make it persistent)

# read()
    # reads one object
    def read_one_object(self, table):
        one_query = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = one_query.fetchone()
            if record is None:
                break
            print(record)

# Destroy
    # one object
    def destroy_one_object(self, table, ID, number):
        dropping_query = self.__filter_query(f"DELETE FROM {table} WHERE {ID} = {number}").fetchone()
        return dropping_query


