from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'

db = SQLAlchemy(app)

ma = Marshmallow(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String)
    description = db.Column(db.String(300))
    ingredients = db.Column(db.String(300))
    directions = db.Column(db.String(3000))

    def __repr__(self):
        return '%s' % self.meal


class RecipeSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'meal',
            'description',
            'ingredients',
            'directions'
        )


recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)


@app.route('/api_v2/recipes/', methods=['GET'])
def read_recipes():
    recipes = Recipe.query.all()
    result = recipes_schema.dump(recipes)
    return jsonify(result)


@app.route('/api_v2/recipes/<int:recipe_id>', methods=['GET'])
def retrieve_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return recipe_schema.jsonify(recipe)
