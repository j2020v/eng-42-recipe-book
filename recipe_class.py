import pyodbc

server = 'localhost,1433'
database = 'recipes_db'
username = 'SA'
password = 'Passw0rd2018'

conn_rdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)

cursor = conn_rdb.cursor()
# Define a class recipe

class Recipe():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_rdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_rdb.cursor()


    def __filter_query(self, query):
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.__filter_query(query).execute(query)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    # reads all objects
    def list_all_recipes(self, table):
        all_recipes_query = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = all_recipes_query.fetchone()
            if record is None:
                break
            return record

    # read()
    # reads one object
    def read_one_recipe(self, table, ID, number):
        query = self.__filter_query(f"SELECT * FROM {table} WHERE {ID} = {number}")
        while True:
            record = query.fetchone()
            if record is None:
                break
            return record

    # new()
    # create a recipe object
    def create_recipe(self, recipe_id, recipe_name, ingredients, describe_recipe, instructions, postcode):
        (cursor.execute(f"INSERT INTO recipes ({recipe_id}, {recipe_name},{ingredients}, {describe_recipe},{instructions}, {postcode})"))
        conn_rdb.commit()

# save()
    # saves a recipe object to the DB (make it persistent)

# destroy
    # one object
    def destroy_a_query(self, table, recipe_id):
        dropping_query = self.__filter_query(f"DELETE FROM {table} WHERE ID = {recipe_id}")
        return dropping_query
