# 🧠 Meal Suggestion Expert System

A rule-based expert system built using [`experta`](https://github.com/ibm/experta) that recommends meals based on available ingredients, meal time (e.g. breakfast, lunch), and preparation time constraints.

## 📌 Features

- 💡 Intelligent meal suggestions based on user facts
- ⏱️ Supports maximum cooking time filtering
- 🍳 Ingredient-based rule matching (exact match)
- 📄 Easy-to-extend rule base with new meals and constraints

---

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **Knowledge Engine**: [Experta](https://github.com/ibm/experta)

---

## 🧩 How It Works

The system uses facts such as:

- Available ingredients
- Desired meal time (e.g. `"breakfast"`)
- Max preparation time (e.g. `30 minutes`)

Based on rules, it recommends a matching meal.

---

## 🧪 Sample Usage

### 🔧 1. Install dependencies

```bash
pip install experta
```

---

### 🧠 2. Declare Meals

Inside the script, define your meal dataset:

```python
meals = [
    {
        "name": "Shakshuka",
        "main_ingredients": ["eggs", "tomatoes", "onion", "bell pepper"],
        "optional_ingredients": ["feta cheese", "parsley", "cumin", "paprika"],
        "meal_time": "breakfast",
        "time_required": 25,
    },
    # Add more meals...
]
```

---

### 🧑‍🍳 3. Provide User Input (Facts)

```python
engine.declare(Ingredient(name='eggs'))
engine.declare(Ingredient(name='tomatoes'))
engine.declare(Ingredient(name='onion'))
engine.declare(Ingredient(name='bell pepper'))
engine.declare(MealTime(value='breakfast'))
engine.declare(MaxTime(value=30))
```

---

### ▶️ 4. Run the Engine

```python
for m in meals:
    engine.declare(Meal(**m))

engine.run()
```

---

### ✅ Sample Output

```
Suggested meal: Shakshuka (takes 25 minutes)
```

---

## 📦 Project Structure

```
meal-suggester/
├── main.py           # Main logic for the expert system
├── README.md         # Documentation
├── requirements.txt  # List of Python dependencies
```

---

## 📌 Extending the System

To add more rules or meals:
- Add new entries to the `meals` array.
- Update rule logic if needed (e.g. for partial matching or preferences like vegetarian).

To integrate into a GUI or API:
- Extract input from user forms
- Feed inputs as `Ingredient`, `MealTime`, and `MaxTime` facts
- Show results from engine output

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork and submit a pull request.

---

## 👨‍💻 Author

**Abdul Majid Al-Shami**  
Built using [Experta](https://github.com/ibm/experta) with ❤️ for smart food recommendations.