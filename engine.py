from rules import MealSuggester
from facts import Ingredient, MealTime, MaxTime, Meal, UserInput

engine = MealSuggester()
engine.reset()

# Declare user's available ingredients
user_input = UserInput(
    ingredients={
        'chickpeas',
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
    },
    health_conditions=[],
    meal_type="lunch",
    people=1,
)

engine.declare(user_input)


engine.run()
# engine.show_results()
