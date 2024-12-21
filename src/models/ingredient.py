class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"{self.quantity} {self.unit} of {self.name}"