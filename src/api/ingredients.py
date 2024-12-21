from flask import Blueprint, request, jsonify
from services.ingredient_service import add_ingredient, update_ingredient, get_all_ingredients

ingredients_blueprint = Blueprint('ingredients', __name__)

@ingredients_blueprint.route('/', methods=['GET'])
def get_ingredients():
    ingredients = get_all_ingredients()
    return jsonify([ingredient.to_dict() for ingredient in ingredients])

@ingredients_blueprint.route('/', methods=['POST'])
def create_ingredient():
    data = request.get_json()
    new_ingredient = add_ingredient(data['name'], data['quantity'], data['unit'])
    return jsonify(new_ingredient.to_dict()), 201

@ingredients_blueprint.route('/<int:ingredient_id>', methods=['PUT'])
def modify_ingredient(ingredient_id):
    data = request.get_json()
    updated_ingredient = update_ingredient(ingredient_id, data['quantity'])
    if updated_ingredient:
        return jsonify(updated_ingredient.to_dict())
    return jsonify({'error': 'Ingredient not found'}), 404