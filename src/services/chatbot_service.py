from flask import request, jsonify
from models.recipe import Recipe
from services.recipe_service import get_recipes_based_on_ingredients
from openai import ChatCompletion as LLMChatbot  # Example replacement, adjust as needed

class ChatbotService:
    def __init__(self):
        self.chatbot = LLMChatbot()

    def process_user_input(self, user_input):
        # Process the user input to understand preferences
        if "sweet" in user_input:
            return "You want something sweet!"
        # Add more preference processing as needed
        return "What type of dish are you craving?"

    def recommend_recipes(self, available_ingredients):
        recipes = get_recipes_based_on_ingredients(available_ingredients)
        if not recipes:
            return "Sorry, I couldn't find any recipes with those ingredients."
        return recipes

def chatbot_interaction():
    user_input = request.json.get("input")
    available_ingredients = request.json.get("ingredients", [])
    
    chatbot_service = ChatbotService()
    preference_response = chatbot_service.process_user_input(user_input)
    recipe_recommendations = chatbot_service.recommend_recipes(available_ingredients)
    
    return jsonify({
        "preference_response": preference_response,
        "recipe_recommendations": recipe_recommendations
    })