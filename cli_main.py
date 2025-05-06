import recipe_fetcher as rf
import ingredients_fetcher 


menu = "========Menu========\n1.Input\n0.Exit"
list_of_moods = "1. Happy\n2. Sad\n3. Anxious\n4. Tired/ Drowsy\n5. Hungry"
list_of_cravings ="1. Sweet\n2. Salty\n3. Spicy\n4. Sour\n5. Crunchy/ Oily"

recipe_lookup, _ = rf.load_recipe_index()

while True:
    print(menu)
    menu_opt = int(input("Enter option: "))

    if menu_opt == 1:
        print(list_of_moods)
        mood = int(input())
        print(list_of_cravings)
        craving = int(input())
        ingredients = ingredients_fetcher.fetch(mood, craving)

        print(ingredients)
        matched_ids = rf.find_recipe_numbers(ingredients, recipe_lookup)
        if not matched_ids:
            print("No matching recipes found.")
        else:
            rf.fetch_and_save_recipes(matched_ids)
            print(f"Recipes saved to 'matching_recipes.csv'.")
    elif menu_opt == 0:
        print("Exiting...")
        break
    