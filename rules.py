from experta import KnowledgeEngine, Rule, MATCH, TEST, AS
from facts import MealTime, MaxTime, Meal, Ingredient


class MealSuggester(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.suggestions = []

    @Rule(
        Meal(
            name=MATCH.name,
            main_ingredients=MATCH.req_ings,
            optional_ingredients=MATCH.opt_ings,
            meal_time=MATCH.meal_time,
            time_required=MATCH.time_needed,
        ),
        MealTime(value=MATCH.time),
        MaxTime(value=MATCH.max_time),
        TEST(lambda time_needed, max_time: time_needed <= max_time),
    )
    def suggest_meal(
        self, name, req_ings, opt_ings, meal_time, time, time_needed, max_time
    ):
        user_ings = [
            fact["name"] for fact in self.facts.values() if isinstance(fact, Ingredient)
        ]

        matched = [i for i in req_ings if i in user_ings]
        missing = [i for i in req_ings if i not in user_ings]
        match_ratio = len(matched) / len(req_ings)

        # Set threshold (e.g. at least 60% of ingredients matched)
        if time == meal_time and match_ratio >= 0.6:
            self.suggestions.append(
                {
                    "name": name,
                    "matched": matched,
                    "missing": missing,
                    "match_score": match_ratio,
                    "time_needed": time_needed,
                }
            )

    def show_results(self):
        # Sort by match_score descending, then by time ascending
        sorted_meals = sorted(
            self.suggestions, key=lambda m: (-m["match_score"], m["time_needed"])
        )
        if not sorted_meals:
            print("No suitable meals found with current ingredients.")
            return

        print("Suggested Meals (Best Matches First):\n")
        for m in sorted_meals:
            print(
                f"- {m['name']} (Time: {m['time_needed']} mins, Match: {round(m['match_score']*100)}%)"
            )
            print(f"Matched ingredients: {m['matched']}")
            print(f"Missing ingredients: {m['missing']}\n")
