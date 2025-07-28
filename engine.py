from rules import MealSuggester
from facts import Ingredient, MealTime, MaxTime, Meal
from meals_db import meals

engine = MealSuggester()
engine.reset()

# Declare user's available ingredients
user_ingredients = [
    "eggs",
    "tomatoes",
    "bell pepper",
    "parsley",
    "coconut milk",
    "curry powder",
    "flour",
    "eggs",
    "milk",
    "baking powder",
]
for ing in user_ingredients:
    engine.declare(Ingredient(name=ing))

# Declare preferences
engine.declare(MealTime(value="breakfast"))
engine.declare(MaxTime(value=30))

# Declare meals
for m in meals:
    engine.declare(Meal(**m))

engine.run()
engine.show_results()
