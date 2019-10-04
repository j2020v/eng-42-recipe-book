from recipe_class import *

# List all recipes
conn_rdb = Recipe(server, database, username, password)
print(conn_rdb.list_all_recipes("recipes"))

# read one object
conn_rdb = Recipe(server, database, username, password)
query = (conn_rdb.read_one_recipe("recipes", "recipe_id", "2"))
print(query)

# add a recipe NEED HELP ON ADDING !!!
# conn_rdb = Recipe(server, database, username, password)
# (conn_rdb.create_recipe("3", "'Peanut Butter banana'", "'Peanut butter and banana'", "'Amazing dessert'", "'Dip banana into peanut butter jar'", "'KT2 6EL'"))

# export recipe to a txt file
conn_rdb.open_read_file_using_with = 'recipes.txt'


