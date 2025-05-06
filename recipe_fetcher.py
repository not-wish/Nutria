import pandas as pd
from collections import defaultdict
from fuzzywuzzy import process

CSV_PATH = "RAW_recipes.csv"
OUTPUT_FILE = "matching_recipes.csv"

# Step 1: Load only recipe numbers and ingredients
def load_recipe_index():
    df_index = pd.read_csv(CSV_PATH, usecols=["id", "ingredients"], dtype=str)
    df_index['ingredients'] = df_index['ingredients'].apply(lambda x: set(eval(x)))
    
    recipe_lookup = defaultdict(set)
    for _, row in df_index.iterrows():
        for ingredient in row['ingredients']:
            recipe_lookup[ingredient.lower()].add(row['id'])
    return recipe_lookup, df_index

# Step 2: Find recipes based on ingredients (with fuzzy matching for similar ingredients)
def find_recipe_numbers(user_ingredients, recipe_lookup):
    matched_recipes = set()
    
    for ingredient in user_ingredients:
        ingredient = ingredient.lower()
        # Exact match
        if ingredient in recipe_lookup:
            matched_recipes.update(recipe_lookup[ingredient])
        else:
            # Fuzzy match (find closest ingredients)
            closest_match, score = process.extractOne(ingredient, recipe_lookup.keys())
            if score > 80:  # Consider it a match if similarity is high
                matched_recipes.update(recipe_lookup[closest_match])
    
    return matched_recipes

# Step 3: Load matching recipes and save to CSV
def fetch_and_save_recipes(matched_recipe_ids):
    df_full = pd.read_csv(CSV_PATH)
    matched_recipes = df_full[df_full['id'].astype(str).isin(matched_recipe_ids)]
    matched_recipes.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(matched_recipes)} matching recipes to {OUTPUT_FILE}")

# Main Execution

