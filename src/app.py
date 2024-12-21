from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.ingredients import ingredients_blueprint
from api.recipes import recipes_blueprint
from api.chatbot import chatbot_blueprint
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mofas_kitchen_buddy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

# Register blueprints
app.register_blueprint(ingredients_blueprint, url_prefix='/ingredients')
app.register_blueprint(recipes_blueprint, url_prefix='/recipes')
app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot')

if __name__ == '__main__':
    app.run(debug=True)