from flask import Blueprint, request, jsonify
from services.chatbot_service import ChatbotService

chatbot_blueprint = Blueprint('chatbot', __name__)

@chatbot_blueprint.route('/recommend', methods=['POST'])
def recommend_recipe():
    data = request.json
    ingredients = data.get('ingredients', [])
    preference = data.get('preference', '')

    if not ingredients:
        return jsonify({'error': 'No ingredients provided'}), 400

    chatbot_service = ChatbotService()
    recommendations = chatbot_service.recommend_recipes(ingredients)
    return jsonify(recommendations), 200