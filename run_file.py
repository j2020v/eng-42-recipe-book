from connection import *
from recipe_class import *

server = 'localhost,1433'
database = 'my_recipes'
username = 'SA'
password = 'Passw0rd2018'

conn_recipe = Recipe(server, database, username, password)

#adding a recipe
#conn_recipe.create_recipe(4, "'Nutella pancakes'", "'Flour, egg and nutella'", "'For the sweet tooth'", "'Mix flour, egg and nutella until sticky and fry'", "'HA55NZ'")

#delete a query
#conn_recipe.destroy_query("dbo.recipes", 4)

#list all recipes
#print(conn_recipe.list_all_recipes("dbo.recipes"))

#read one object
#print(conn_recipe.read_one_recipe("dbo.recipes", 3))

#export recipe to a txt file
#conn_recipe.write_one_recipe_to_txt(3)

#update object
#conn_recipe.update_recipe("dbo.recipes", "name", "'PB & J'", 2)

#more info on the location of the recipe where the recipe was created (postcode)
#conn_recipe.recipe_info(3)










