import json

import pyodbc

from db_connect import cursor, conn_rdb

server = 'localhost,1433'
database = 'recipes_db'
username = 'SA'
password = 'Passw0rd2018'

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

    def open_read_file_using_with(file):
        try:
            with open(file, 'r') as recipes:  # does not need to close method
                for line in recipes.readlines():
                    print(line.rstrip('\n'))
        except FileNotFoundError as errmsg:
            print('There has been a syntax error', errmsg)
            raise
        finally:
            print('\n Execution_completed')
# save()
    # saves a recipe object to the DB (make it persistent)



# Destroy
    # one object