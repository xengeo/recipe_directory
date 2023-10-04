# File: test:test_recipe_repository.py

from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
Test when we run RecipeRepository#all
We receive a list of Recipe objects 
reflecting the seed data
"""
def test_all_returns_expected_result_set(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'Chicken Curry', 40 , 3),
        Recipe(2, 'Beef Pie', 25 , 2),
        Recipe(3, 'Roast Chicken', 60 , 4),
        Recipe(4, 'Steak', 10 , 5),
        Recipe(5, 'Ratatouille', 50 , 4)
    ]


"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_find_returns_recipe_object(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)

    results = repository.find(4)
    
    assert results == Recipe(4, 'Steak', 10 , 5)