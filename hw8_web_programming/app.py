from flask import Flask, abort, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


RECIPES = [
    {
        "id": 1,
        "meal": "Easy Meatloaf",
        "description": "This is a very easy and no fail recipe for meatloaf. "
                       "It won't take long to make at all, and it's quite good!",
        "ingredients": "ground beef, 1 egg, 1 onion, 1 cup milk, etc.",
        "directions": "Preheat oven to 350 degrees F (175 degrees C).\nIn a large bowl, "
                      "combine the beef, egg, onion, milk and bread OR cracker crumbs. "
                      "Season with salt and pepper to taste and place in a lightly greased "
                      "9x5-inch loaf pan, or form into a loaf and place in a lightly greased "
                      "9x13-inch baking dish.\nIn a separate small bowl, combine the brown sugar, "
                      "mustard and ketchup. Mix well and pour over the meatloaf.\nBake at 350 "
                      "degrees F (175 degrees C) for 1 hour."
    }
]


@app.route('/api/recipes/', methods=['GET'])
def read_recipes():
    return jsonify(RECIPES)


@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def retrieve_recipe(recipe_id):
    recipe = [recipe for recipe in RECIPES if recipe.get('id') == recipe_id]
    if not recipe:
        abort(404)
    else:
        return jsonify(recipe)


@app.route('/api/recipes/', methods=['POST'])
def create_recipe():
    if 'meal' in request.json and \
       'description' in request.json and \
       'ingredients' in request.json and \
       'directions' in request.json:
        recipe = {
            'id': request.json.get('id', RECIPES[-1]['id'] + 1),
            'meal': request.json['meal'],
            'description': request.json['description'],
            'ingredients': request.json['ingredients'],
            'directions': request.json['directions']
        }
        return recipe, 201
    else:
        abort(400)


@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe():
    """Think and rewrite"""
    if 'meal' in request.json and \
       'description' in request.json and \
       'ingredients' in request.json and \
       'directions' in request.json:
        recipe = {
            'id': request.json.get('id', RECIPES[-1]['id'] + 1),
            'meal': request.json['meal'],
            'description': request.json['description'],
            'ingredients': request.json['ingredients'],
            'directions': request.json['directions']
        }
        return recipe, 200
    else:
        abort(400)
