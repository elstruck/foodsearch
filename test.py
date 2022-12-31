#random document for testing scripts
import spoonacular as sp
import requests
api_key = "cf67ce89c4d84834a148628ef62e2486"

#user input for ingredients
param1 = input("Search for recipes by ingredient:")

#spoonacular api requests
byingredients = "https://api.spoonacular.com/recipes/findByIngredients?apiKey={}&ingredients=param1={}&number=2".format(api_key, param1)


response = requests.get(byingredients)
print(response.json)