from flask import Blueprint, request, jsonify
from services.recipe_service import add_recipe_to_file, get_recipes_based_on_ingredients, parse_recipes_from_file
from models.recipe import Recipe
import os

recipes_blueprint = Blueprint('recipes', __name__)

# Define the path to the recipes file
recipes_file_path = os.path.join(os.path.dirname(__file__), 'recipes.txt')

@recipes_blueprint.route('/', methods=['GET'])
def get_recipes():
    try:
        recipes = parse_recipes_from_file(recipes_file_path)
        return jsonify([recipe.to_dict() for recipe in recipes])
    except FileNotFoundError:
        return jsonify({'error': 'Recipes file not found'}), 404

@recipes_blueprint.route('/', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        preparation_time=data['preparation_time'],
        cuisine_type=data['cuisine_type'],
        taste=data['taste']
    )
    add_recipe_to_file(recipes_file_path, new_recipe)
    return jsonify(new_recipe.to_dict()), 201

@recipes_blueprint.route('/suggest', methods=['POST'])
def suggest_recipes():
    data = request.get_json()
    available_ingredients = data['ingredients']
    try:
        recipes = parse_recipes_from_file(recipes_file_path)
        suggested_recipes = get_recipes_based_on_ingredients(available_ingredients, recipes)
        return jsonify([recipe.to_dict() for recipe in suggested_recipes])
    except FileNotFoundError:
        return jsonify({'error': 'Recipes file not found'}), 404