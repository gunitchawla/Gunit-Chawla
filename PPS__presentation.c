FOOD HABIT AND CALORIE ANALYSIS

C- CODE

printf("Welcome to the Food Habit and Calorie Analysis Program!\n");

while (1) {
    printf("Enter a food item (or type 'done' to finish): ");
    scanf("%s", foodItem);

    if (strcmp(foodItem, "done") == 0) {
        break;
    }

    int calories = findCalories(foodItem);
    if (calories != -1) {
        printf("Added %s - Calories: %d\n", foodItem, calories);
        totalCalories += calories;
    } else {
        printf("Food item not found. Please enter a valid food item.\n");
    }
}

printf("\nTotal Calories Consumed: %d\n", totalCalories);

// Basic analysis
if (totalCalories > 2500) {
printf("Warning: High calorie intake! Consider consulting a nutritionist.\n");
} else if (totalCalories < 1500) {
    printf("Warning: Low calorie intake! Ensure you're meeting your nutritional needs.\n");
}

return 0;
}








