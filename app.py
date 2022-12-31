from flask import Flask, render_template, request

import requests
app = Flask(__name__)
app.debug = True

url = "https://api.spoonacular.com/"

apiKey = "?apiKey=cf67ce89c4d84834a148628ef62e2486"

find = "recipes/findByIngredients"
randomFind = "recipes/random"

@app.route('/home')
def home_page():
  return render_template('homepage.html')

@app.route('/')
def search_page():
  return render_template('search.html')

@app.route('/recipes', methods=["POST"])
def get_recipes():
    ingridients = request.form.getlist('search')
    if (len('ingridients')) > 0:
        # If there is a list of ingridients -> list     
        ingrids_string = ",+".join(ingridients)   
        ingrids_string = "&ingredients=" + ingrids_string
        response = requests.request("GET", "".join([str(url), find, apiKey, ingrids_string])).json()
        return render_template('recipes.html', recipes=response)
    else:
        # Random recipes
        response = requests.request("GET", "".join([str(url), randomFind, apiKey])).json()
        return render_template('recipes.html', recipes=response['recipes'])

@app.route('/recipe')
def get_recipe():
  recipe_id = request.args['id']
  recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)

  recipe_info = requests.request("GET", "".join([str(url), recipe_info_endpoint, apiKey])).json()
 
  querystring = {"defaultCss":"true", "showBacklink":"false"}
 
  return render_template('recipe.html', recipe=recipe_info)

if __name__ == '__main__':
  app.run()