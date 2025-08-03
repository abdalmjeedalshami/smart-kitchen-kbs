from experta import Fact


class Ingredient(Fact):
    name: str


class MealTime(Fact):
    value: str


class MaxTime(Fact):
    value: int


class Meal(Fact):
    name: str
    main_ings: set
    optional_ings: set
    meal_type: str
    time_required: int
    score: float


class UserInput(Fact):
    ingredients: list
    health_conditions: list
    meal_type: str
    people: int
