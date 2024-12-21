class Recipe:
    def __init__(self, title, ingredients, preparation_time, cuisine_type, taste):
        self.title = title
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cuisine_type = cuisine_type
        self.taste = taste

    def to_dict(self):
        return {
            'title': self.title,
            'ingredients': self.ingredients,
            'preparation_time': self.preparation_time,
            'cuisine_type': self.cuisine_type,
            'taste': self.taste
        }