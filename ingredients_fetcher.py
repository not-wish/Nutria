list_of_moods = ["", "Happy", "Sad", "Anxious", "Tired", "Hungry"]
list_of_cravings = ["", "Sweet", "Salty", "Spicy", "Sour", "Crunchy"]
list_of_minerals = {
        "Happy": ["Magnesium", "Vitamin D", "Omega-3", "Zinc"],
        "Sad": ["Omega-3", "B Vitamins", "Iron", "Magnesium"],
        "Anxious": ["Magnesium", "Zinc", "Vitamin B6", "Calcium"],
        "Tired": ["Iron", "Magnesium", "Potassium", "B Vitamins"],
        "Hungry": ["Chromium", "Zinc", "Magnesium", "Omega-3"],
        "Sweet": ["Magnesium", "Chromium", "Zinc", "Tryptophan"],
        "Salty": ["Sodium", "Chloride", "Potassium", "Calcium"],
        "Spicy": ["Zinc", "Iron", "Sulfur", "Capsaicin"],
        "Sour": ["Magnesium", "Vitamin C", "Calcium", "Potassium"],
        "Crunchy": ["Silicon", "Calcium", "Magnesium", "Zinc"]
}

def fetch(mood, craving):
    minerals = mineral_fetcher(mood)
    minerals_craving = mineral_fetcher(craving)

    ingredients = fetch_ingredients(set.intersection(minerals, minerals_craving))
    return ingredients

def mineral_fetcher(need):
    return set(list_of_minerals[need])

ingredients = {
    "Magnesium": [
        "Spinach", "Almonds", "Pumpkin seeds", "Dark chocolate", "Avocado", 
        "Cashews", "Black beans", "Quinoa", "Tofu", "Whole wheat bread", 
        "Brown rice", "Salmon", "Bananas", "Yogurt", "Figs"
    ],
    "Vitamin D": [
        "Salmon", "Mushrooms", "Egg yolks", "Fortified milk", "Sardines", 
        "Tuna", "Cod liver oil", "Fortified orange juice", "Shrimp", 
        "Oysters", "Fortified cereals", "Pork chops", "Beef liver", 
        "Caviar", "Herring"
    ],
    "Omega-3": [
        "Salmon", "Chia seeds", "Walnuts", "Flaxseeds", "Mackerel", 
        "Anchovies", "Sardines", "Hemp seeds", "Cod liver oil", 
        "Soybeans", "Brussels sprouts", "Algal oil", "Oysters", 
        "Seaweed", "Eggs (fortified)"
    ],
    "Zinc": [
        "Oysters", "Beef", "Chickpeas", "Pumpkin seeds", "Cashews", 
        "Lentils", "Yogurt", "Chicken", "Turkey", "Quinoa", 
        "Mushrooms", "Spinach", "Dark chocolate", "Whole grains", 
        "Crab"
    ],
    "B Vitamins": [
        "Eggs", "Lentils", "Leafy greens", "Whole grains", "Milk", 
        "Chicken", "Salmon", "Avocado", "Sunflower seeds", "Beef liver", 
        "Nutritional yeast", "Pork", "Bananas", "Potatoes", "Legumes"
    ],
    "Iron": [
        "Red meat", "Lentils", "Spinach", "Tofu", "Quinoa", 
        "Chickpeas", "Pumpkin seeds", "Turkey", "Broccoli", 
        "Dark chocolate", "Sardines", "Beef liver", "Oysters", 
        "Kidney beans", "Fortified cereals"
    ],
    "Vitamin B6": [
        "Bananas", "Chicken", "Tuna", "Potatoes", "Sunflower seeds", 
        "Chickpeas", "Salmon", "Turkey", "Avocado", "Spinach", 
        "Walnuts", "Beef", "Fortified cereals", "Pistachios", 
        "Dried prunes"
    ],
    "Calcium": [
        "Milk", "Cheese", "Yogurt", "Kale", "Almonds", 
        "Broccoli", "Sardines", "Fortified plant-based milk", 
        "Tofu (calcium-set)", "Oranges", "Figs", "White beans", 
        "Canned salmon", "Bok choy", "Collard greens"
    ],
    "Potassium": [
        "Bananas", "Sweet potatoes", "Spinach", "Oranges", 
        "Coconut water", "Avocado", "Potatoes", "Beets", 
        "Pumpkin", "White beans", "Salmon", "Edamame", 
        "Pomegranate", "Mushrooms", "Cantaloupe"
    ],
    "Chromium": [
        "Broccoli", "Grapes", "Whole grains", "Potatoes", 
        "Green beans", "Garlic", "Basil", "Orange juice", 
        "Turkey", "Beef", "Apples", "Bananas", "Eggs", 
        "Brazil nuts", "Oats"
    ],
    "Tryptophan": [
        "Turkey", "Chicken", "Milk", "Nuts", "Seeds", 
        "Cheese", "Eggs", "Salmon", "Tofu", "Pumpkin seeds", 
        "Sesame seeds", "Oats", "Beans", "Lentils", 
        "Spirulina"
    ],
    "Sodium": [
        "Salt", "Seaweed", "Cheese", "Pickles", "Olives", 
        "Canned soups", "Soy sauce", "Cured meats", 
        "Pretzels", "Crackers", "Bread", "Tomato juice", 
        "Cottage cheese", "Pizza", "Bagels"
    ],
    "Chloride": [
        "Salt", "Seaweed", "Celery", "Tomatoes", "Lettuce", 
        "Olives", "Rye", "Kelp", "Sea salt", "Cucumber", 
        "Zucchini", "Eggplant", "Bell peppers", "Cabbage", 
        "Asparagus"
    ],
    "Sulfur": [
        "Garlic", "Onions", "Eggs", "Broccoli", "Cabbage", 
        "Brussels sprouts", "Kale", "Cauliflower", "Radishes", 
        "Turnips", "Leeks", "Shallots", "Fish", "Meat", 
        "Legumes"
    ],
    "Vitamin C": [
        "Oranges", "Bell peppers", "Strawberries", "Kiwi", 
        "Tomatoes", "Broccoli", "Brussels sprouts", 
        "Pineapple", "Papaya", "Guava", "Kale", "Lemon", 
        "Lime", "Cauliflower", "Mango"
    ],
    "Silicon": [
        "Bananas", "Brown rice", "Oats", "Beer", "Green beans", 
        "Spinach", "Whole grains", "Carrots", "Cucumber", 
        "Almonds", "Hazelnuts", "Apples", "Oranges", 
        "Strawberries", "Beets"
    ]
}

def fetch_ingredients(mineral_set):
    ingredient_list = set()
    for mineral in mineral_set:
        ingredient_list.update(ingredients.get(mineral, []))
    return ingredient_list