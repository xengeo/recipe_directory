from lib.recipe import Recipe

"""
Test recipe can be initialised with
id, name, average_cooking_time, rating
"""
def test_recipe_cane_be_initialised():
    recipe = Recipe(1, 'Test Name', 10, 4)
    assert recipe.id == 1
    assert recipe.name == 'Test Name'
    assert recipe.average_cooking_time == 10
    assert recipe.rating == 4

"""
Test expected object is equal to actual object
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_identical():
    recipe_1 = Recipe(1, 'Test Name', 10, 4)
    recipe_2 = Recipe(1, 'Test Name', 10, 4)
    assert recipe_1 == recipe_2


"""
Test recipe formats nicely
"""
def test_recipe_formats_nicely():
    recipe_1 = Recipe(1, 'Test Name', 10, 4)
    assert str(recipe_1) == "Recipe(1, Test Name, 10, 4)"