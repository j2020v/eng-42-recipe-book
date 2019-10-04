from connection import *
import json
import requests

class Recipe(ConnectionMicrosoftServer):


    def list_all_recipes(self, table):
        query = self.filter_query(f"SELECT * FROM {table}")
        while True:
            record = query.fetchall()
            if record is None:
                break
            return record

    # read()
    # reads one object
    def read_one_recipe(self, table, recipe_id):
        query = self.filter_query(f"SELECT * FROM {table} WHERE recipe_id = {recipe_id}")
        while True:
            record = query.fetchone()
            if record is None:
                break
            return record

    # new()
    # create a recipe object
    def create_recipe(self, recipe_id, recipe_name, ingredients, describe_recipe, instructions, postcode):
        query_rows = self.filter_query(f"INSERT INTO recipes VALUES ({recipe_id}, {recipe_name},{ingredients}, {describe_recipe},{instructions}, {postcode})")
        self.conn_rdb.commit()

    # destroy
    # one object
    def destroy_query(self, table, recipe_id):
        query_rows = self.filter_query(f"DELETE FROM {table} WHERE recipe_id = {recipe_id}")
        self.conn_rdb.commit()

    # exporting recipe to a txt file
    def write_one_recipe_to_txt(self, recipe_id):
        query_rows = self.filter_query(f"SELECT * FROM recipes WHERE recipe_id = {recipe_id}")
        string_query = str(query_rows.fetchone())
        try:
            with open('recipes.txt', 'a') as opened_file:
                opened_file.write(string_query)
        except FileNotFoundError:
            print('File not found')

    # update object
    def update_recipe(self, table, column, value, recipe_id):
        query_rows = self.filter_query(f"UPDATE {table} SET {column} = {value} WHERE recipe_id = {recipe_id}")
        self.conn_rdb.commit()

    # more info on the location
    def recipe_info(self, recipe_id):
        query_rows = self.filter_query(f"SELECT postcode FROM dbo.recipes WHERE recipe_id = {recipe_id}")
        postcode_query = query_rows.fetchone()
        postcode = ' '.join([row for row in postcode_query])
        url = 'https://postcodes.io/postcodes/'
        request_postcode = requests.get(url + postcode)
        post_code_dict = request_postcode.json()
        details = post_code_dict
        print(details)

    #get some more info about ingredients 






