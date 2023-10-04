# File: lib/recipe_repository.py

from lib.recipe import Recipe

class RecipeRepository:

    def __init__(self, connection) -> None:
        """Initialise attributes"""
        # parameters: db_connection
        # Returns: Nothing
        # Side-effects: Assigns to instance var connection
        self._connection = connection

    def all(self):
        """Retrieve all recipes"""
        # Parameters: None
        # Returns: List of recipe class instances
        # Side-effects: Runs db_connection class execute function
        # to retreive results
        rows = self._connection.execute('SELECT * FROM recipes')

        recipes = []
        for row in rows:
            recipe = Recipe(
                            row['id'], 
                            row['name'], 
                            row['average_cooking_time'], 
                            row['rating']
                            )
            recipes.append(recipe)
        return recipes    
        

    def find(self, id):
        """Find specific recipe from DB using and id"""
        # Parameters: id
        # Returns: Instance of that recipe
        # Side-effects: Runs db_connection class execute function
        # to retreive results
        results = self._connection.execute(
            'SELECT * FROM recipes WHERE id = %s', [id]
            )
        row = results[0]
        return Recipe(row['id'], 
                      row['name'], 
                      row['average_cooking_time'], 
                      row['rating'])