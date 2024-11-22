Python Code--

food_calories = { 'apple': 95, 'banana': 105, 'orange': 62, 'bread': 79, 'rice': 206, 'chicken': 335, 'fish': 232, 'potato': 161, 'cheese': 113, 'milk': 103, }
def main(): print("Welcome to the Food Habit and Calorie Analysis Program!")

total_calories = 0
food_log = []

while True:
    food_item = input("Enter a food item (or type 'done' to finish): ").lower()
    
    if food_item == 'done':
        break
    
    if food_item in food_calories:
        food_log.append(food_item)
        total_calories += food_calories[food_item]
        print(f"Added {food_item} - Calories: {food_calories[food_item]}")
    else:
        print("Food item not found. Please enter a valid food item.")

print("\n--- Food Log ---")
for item in food_log:
    print(f"{item.title()} - Calories: {food_calories[item]}")

print(f"\nTotal Calories Consumed: {total_calories}")

# Basic analysis
if total_calories > 2500:  # Adjust based on average daily intake for adults
    print("Warning: High calorie intake! Consider consulting a nutritionist.")
elif total_calories < 1500:
    print("Warning: Low calorie intake! Ensure you're meeting your nutritional needs.")
    if name == "main": main()
