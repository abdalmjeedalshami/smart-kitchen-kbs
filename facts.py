from experta import Fact

class Ingredient(Fact):
    name: str

class MealTime(Fact):
    value: str

class MaxTime(Fact):
    value: int

class Meal(Fact):
    name: str
    main_ingredients: list
    optional_ingredients: list
    meal_time: str
    time_required: int
