# File: lib/recipe.py

"""Class to encapsulate recipes"""


class Recipe:

    def __init__(self, id, name, average_cooking_time, rating) -> None:
        # Parameters: id, name, average_cooking_time, rating
        # Returns: Nothing
        # Side-effects: Assigns parameters to instance variables
        # Each parameter is a column in our recipes table in the database "recipe_directory"
        self.id = id
        self.name = name
        self.average_cooking_time = average_cooking_time
        self.rating = rating

    def __eq__(self, other):
        return self.__doc__ == other.__doc__
        

    def __repr__(self) -> str:
        return f"Recipe({self.id}, {self.name}, {self.average_cooking_time}, {self.rating})"