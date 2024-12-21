from models.recipe import Recipe

def parse_recipes_from_file(file_path):
    recipes = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_recipe = None
        for line in lines:
            line = line.strip()
            if line.startswith("Title:"):
                if current_recipe:
                    recipes.append(current_recipe)
                current_recipe = Recipe(title=line.split("Title:")[1].strip(), ingredients=[], preparation_time="", cuisine_type="", taste="")
            elif line.startswith("Ingredients:"):
                if current_recipe:
                    ingredients = line.split("Ingredients:")[1].strip().split(",")
                    current_recipe.ingredients = [ingredient.strip() for ingredient in ingredients]
            elif line.startswith("Preparation Time:"):
                if current_recipe:
                    current_recipe.preparation_time = line.split("Preparation Time:")[1].strip()
            elif line.startswith("Cuisine Type:"):
                if current_recipe:
                    current_recipe.cuisine_type = line.split("Cuisine Type:")[1].strip()
            elif line.startswith("Taste:"):
                if current_recipe:
                    current_recipe.taste = line.split("Taste:")[1].strip()
        if current_recipe:
            recipes.append(current_recipe)
    return recipes

def get_recipes_based_on_ingredients(available_ingredients, recipes):
    suggested_recipes = []
    for recipe in recipes:
        if all(ingredient in available_ingredients for ingredient in recipe.ingredients):
            suggested_recipes.append(recipe)
    return suggested_recipes

def add_recipe_to_file(file_path, recipe):
    with open(file_path, 'a') as file:
        file.write(f"Title: {recipe.title}\n")
        file.write(f"Ingredients: {', '.join(recipe.ingredients)}\n")
        file.write(f"Preparation Time: {recipe.preparation_time}\n")
        file.write(f"Cuisine Type: {recipe.cuisine_type}\n")
        file.write(f"Taste: {recipe.taste}\n\n")