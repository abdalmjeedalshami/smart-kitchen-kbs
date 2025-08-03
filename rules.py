from experta import KnowledgeEngine, Rule, MATCH, TEST, AS
from facts import MealTime, MaxTime, Meal, Ingredient, UserInput
from meals_db import meals


class MealSuggester(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.suggestions = []

    @Rule(
        UserInput(
            ingredients=MATCH.ingredients,
            health_conditions=MATCH.health_conditions,
            meal_type=MATCH.meal_type,
            people=MATCH.people,
        ),
        salience=10,
    )
    def generate_candidates(self, ingredients, health_conditions, meal_type, people):
        for meal in meals:
            main_ings = meal["main_ingredients"]
            if main_ings:
                matched_main_ings = ingredients & main_ings
                main_ings_ratio = len(matched_main_ings) / len(main_ings)

                if main_ings_ratio < 0:
                    continue
            else:
                matched_main_ings = 0
                main_ings_ratio = 1

            optional_ings = meal["optional_ingredients"]
            matched_optional_ings = ingredients & optional_ings
            optional_ings_ratio = len(matched_optional_ings) / max(
                len(optional_ings), 1
            )
            missing = main_ings - ingredients

            self.declare(
                Meal(
                    name=meal["name"],
                    main_ings=main_ings,
                    optional_ings=optional_ings,
                    meal_type=meal["meal_type"],
                    time_required=meal["time_required"],
                    score=0.0,
                )
            )

    @Rule(
        AS.candidate
        << Meal(
            name=MATCH.name,
            main_ings=MATCH.main_ings,
            score=MATCH.score,
        ),
        UserInput(ingredients=MATCH.ingredients),
        salience=5,
    )
    def score_main_ings_matched(self, candidate, name, ingredients, main_ings, score):
        if main_ings:
            matched_main_ings = ingredients & main_ings
            main_ings_ratio = len(matched_main_ings) / len(main_ings)

        else:
            matched_main_ings = 0
            main_ings_ratio = 1

        new_score = score + main_ings_ratio * 100
        # print("This is new score: " , new_score)
        self.modify(candidate, score=new_score)
        print(name, " ", main_ings_ratio)

    # @Rule(Meal(name=MATCH.name, score=MATCH.score), salience=1)
    # def print_specific(self, score, name):
    #     print(name, "score from fact:", score)

    # @Rule(
    #     Meal(
    #         name=MATCH.name,
    #         matched_main_ings=MATCH.matched_main_ings,
    #         matched_optional_ings=MATCH.matched_optional_ings,
    #         meal_type=MATCH.meal_type,
    #         time_required=MATCH.time_required,
    #     ),

    #     TEST(lambda time_required, max_time: time_required <= max_time),
    # )
    # def suggest_meal(
    #     self, name, req_ings, opt_ings, meal_time, time, time_needed, max_time
    # ):
    #     user_ings = [
    #         fact["name"] for fact in self.facts.values() if isinstance(fact, Ingredient)
    #     ]

    #     matched = [i for i in req_ings if i in user_ings]
    #     missing = [i for i in req_ings if i not in user_ings]
    #     match_ratio = len(matched) / len(req_ings)

    #     # Set threshold (e.g. at least 60% of ingredients matched)
    #     if time == meal_time and match_ratio >= 0.6:
    #         self.suggestions.append(
    #             {
    #                 "name": name,
    #                 "matched": matched,
    #                 "missing": missing,
    #                 "match_score": match_ratio,
    #                 "time_needed": time_needed,
    #             }
    #         )

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
