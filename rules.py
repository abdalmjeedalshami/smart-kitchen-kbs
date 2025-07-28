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

        matched = [i for i in req_ings if i in user_ings]
        match_ratio = len(matched) / len(req_ings)

        # Set threshold (e.g. at least 60% of ingredients matched)
        if time == meal_time and match_ratio >= 0.6:
            missing = [i for i in req_ings if i not in user_ings]
            print(f"Suggested meal: {name} (Time: {time_needed} mins)")
            print(f"Matched ingredients: {matched}")
            print(f"Missing ingredients: {missing}\n")
