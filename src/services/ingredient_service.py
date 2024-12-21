from models.ingredient import Ingredient
from database import get_db_session

db_session = get_db_session()

def add_ingredient(name, quantity, unit):
    new_ingredient = Ingredient(name=name, quantity=quantity, unit=unit)
    db_session.add(new_ingredient)
    db_session.commit()
    return new_ingredient

def update_ingredient(ingredient_id, quantity):
    ingredient = db_session.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if ingredient:
        ingredient.quantity = quantity
        db_session.commit()
        return ingredient
    return None

def get_all_ingredients():
    return db_session.query(Ingredient).all()

def get_ingredient_by_name(name):
    return db_session.query(Ingredient).filter(Ingredient.name == name).first()