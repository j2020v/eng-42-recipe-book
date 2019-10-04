from connection import *
from recipe_class import *
server = 'localhost,1433'
database = 'recipes_db'
username = 'SA'
password = 'Passw0rd2018'

conn_rdb = Recipe(server,database,username,password)

# adding a recipe
#conn_rdb.create_recipe(4, "'Nutella pancakes'", "'Flour, egg and nutella'", "'For the sweet tooth'", "'Mix flour, egg and nutella until sticky and fry'", "'HA55NZ'")

# delete a query
#conn_rdb.destroy_query("dbo.recipes", 4)

# list all recipes
#print(conn_rdb.list_all_recipes("dbo.recipes"))

# read one object
#print(conn_rdb.read_one_recipe("dbo.recipes", 3))

# export recipe to a txt file
#conn_rdb.write_one_recipe_to_txt(1)

# update object
#conn_rdb.update_recipe("dbo.recipes", "ingredients", "'mature cheddar and bread'", 2)

# more info on the location of the recipe
conn_rdb.recipe_info(3)









