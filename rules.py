from experta import KnowledgeEngine, Rule, MATCH, TEST, AS
from facts import MealTime, MaxTime, Meal, Ingredient


class MealSuggester(KnowledgeEngine):

    @Rule(
        Meal(
            name=MATCH.name,
            main_ingredients=MATCH.req_ings,
            meal_time=MATCH.meal_time,
            time_required=MATCH.time_needed,
        ),
        MealTime(value=MATCH.time),
        MaxTime(value=MATCH.max_time),
        TEST(lambda time_needed, max_time: time_needed <= max_time),
    )
    def suggest_meal(self, name, req_ings, meal_time, time, time_needed):
        user_ings = [
            fact["name"] for fact in self.facts.values() if isinstance(fact, Ingredient)
        ]
        if all(ing in user_ings for ing in req_ings) and time == meal_time:
            print(f"Suggested meal: {name} (takes {time_needed} minutes)")
