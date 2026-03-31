# SMART diet and workout planner 

def get_user_data():
    print("Welcome to your AI Diet and Fitness Planner.\n")

    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters, e.g., 1.75): "))
    gender = input("Gender (male / female): ").lower()
    goal = input("Your goal (weight_loss / muscle_gain / maintenance): ").lower()
    diet_type = input("Diet preference (veg / non-veg): ").lower()
    activity = input("Activity level (gym / non-gym): ").lower()
    time_slot = input("Preferred workout time (morning / afternoon / evening / night): ").lower()

    print("\nGenerating your personalized plan...\n")

    return age, weight, height, gender, goal, diet_type, activity, time_slot


# ---------- HEALTH ----------
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def body_fat_estimate(bmi, age, gender):
    if gender == "male":
        return round((1.20 * bmi) + (0.23 * age) - 16.2, 2)
    else:
        return round((1.20 * bmi) + (0.23 * age) - 5.4, 2)


# ---------- CALORIES & PROTEIN ----------
def calorie_estimator(weight, goal, activity):
    if goal == "weight_loss":
        calories = weight * 25
    elif goal == "muscle_gain":
        calories = weight * 35
    else:
        calories = weight * 30

    if activity == "gym":
        calories += 200

    return int(calories)


def protein_estimator(weight, goal, activity):
    if goal == "weight_loss":
        protein = weight * 1.2
    elif goal == "muscle_gain":
        protein = weight * 1.8
    else:
        protein = weight * 1.5

    if activity == "gym":
        protein += 10

    return int(protein)


# ---------- SLEEP ----------
def sleep_recommendation(age, goal, activity):
    # base sleep recommendation
    if age < 18:
        sleep_hours = 8.5
    elif age <= 25:
        sleep_hours = 8
    else:
        sleep_hours = 7.5

    # adjust based on goal
    if goal == "muscle_gain":
        sleep_hours += 0.5
    elif goal == "weight_loss":
        sleep_hours += 0.25

    # adjust based on activity
    if activity == "gym":
        sleep_hours += 0.5

    return round(sleep_hours, 1)


def sleep_advice(sleep_hours):
    if sleep_hours >= 8:
        return "Ensure consistent sleep schedule and avoid screens before bedtime."
    else:
        return "Try to improve sleep duration for better recovery and performance."


# ---------- DIET ----------
def generate_meal_plan(calories, diet_type):
    print("Creating a balanced diet plan...\n")

    if calories < 1800:
        portion = "Small"
        factor = 1
    elif calories < 2500:
        portion = "Moderate"
        factor = 1.5
    else:
        portion = "Large"
        factor = 2

    tofu_p = 8 / 100
    spinach_p = 2.9 / 100
    paneer_p = 18 / 100
    dal_p = 9 / 100
    chickpea_p = 19 / 100

    egg_p = 6
    chicken_p = 27 / 100
    fish_p = 25 / 100

    if diet_type == "veg":
        tofu_g = 100 * factor
        dal_g = 80 * factor
        spinach_g = 100 * factor
        chickpea_g = 50 * factor

        breakfast_protein = tofu_g * tofu_p
        lunch_protein = dal_g * dal_p + spinach_g * spinach_p
        dinner_protein = paneer_p * (100 * factor)
        snacks_protein = chickpea_g * chickpea_p

        breakfast = f"Tofu scramble ({tofu_g}g) with multigrain toast | Protein ~{round(breakfast_protein)}g"
        lunch = f"Rice ({100*factor}g) with dal ({dal_g}g) and spinach ({spinach_g}g) | Protein ~{round(lunch_protein)}g"
        dinner = f"Chapati with paneer ({100*factor}g) and salad | Protein ~{round(dinner_protein)}g"
        snacks = f"Roasted chickpeas ({chickpea_g}g) with nuts | Protein ~{round(snacks_protein)}g"

    else:
        eggs = int(2 * factor)
        chicken_g = 150 * factor
        fish_g = 150 * factor

        breakfast_protein = eggs * egg_p
        lunch_protein = chicken_g * chicken_p
        dinner_protein = fish_g * fish_p
        snacks_protein = eggs * egg_p

        breakfast = f"Eggs ({eggs}) with toast | Protein ~{round(breakfast_protein)}g"
        lunch = f"Rice with chicken ({chicken_g}g) | Protein ~{round(lunch_protein)}g"
        dinner = f"Chapati with fish ({fish_g}g) | Protein ~{round(dinner_protein)}g"
        snacks = f"Boiled eggs ({eggs}) | Protein ~{round(snacks_protein)}g"

    return breakfast, lunch, dinner, snacks, portion


# ---------- WORKOUT ----------
def workout_plan(goal, activity, time_slot):
    print("Preparing your workout routine...\n")

    if goal == "weight_loss":
        workout = "Cardio and HIIT (approximately 30 minutes)"
    elif goal == "muscle_gain":
        workout = "Strength training (push, pull, legs split)"
    else:
        workout = "Light cardio with full body exercises"

    if activity == "non-gym":
        workout += " along with home exercises such as push-ups, squats, and plank"

    return f"{time_slot.capitalize()} session: {workout}"


# ---------- OUTPUT ----------
def show_plan(calories, protein, bmi, category, body_fat, sleep_hours, sleep_tip, meals, workout):
    breakfast, lunch, dinner, snacks, portion = meals

    print("\n--- HEALTH SUMMARY ---")
    print(f"BMI: {bmi} ({category})")
    print(f"Estimated Body Fat: {body_fat}%")

    print("\n--- DIET PLAN ---")
    print(f"Calories: {calories} kcal")
    print(f"Protein Target: {protein} g")
    print(f"Portion Size: {portion}")

    print("\nBreakfast:", breakfast)
    print("Lunch:", lunch)
    print("Dinner:", dinner)
    print("Snacks:", snacks)

    print("\n--- WORKOUT PLAN ---")
    print(workout)

    print("\n--- SLEEP RECOMMENDATION ---")
    print(f"Recommended Sleep: {sleep_hours} hours per night")
    print(f"Advice: {sleep_tip}")

    print("\nMaintain consistency across diet, exercise, and sleep for best results.")


# ---------- MAIN ----------
age, weight, height, gender, goal, diet_type, activity, time_slot = get_user_data()

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)
body_fat = body_fat_estimate(bmi, age, gender)

calories = calorie_estimator(weight, goal, activity)
protein = protein_estimator(weight, goal, activity)

sleep_hours = sleep_recommendation(age, goal, activity)
sleep_tip = sleep_advice(sleep_hours)

meals = generate_meal_plan(calories, diet_type)
workout = workout_plan(goal, activity, time_slot)

show_plan(calories, protein, bmi, category, body_fat, sleep_hours, sleep_tip, meals, workout)