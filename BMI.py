# Author: Borong Su
# Date: 230 September 2026
# Description: A simple program for calculating the BMI.

# BMI = weight / (height ** 2)

# BMI = weight / (height ** 2)

try:
    user_weight = float(input("Please enter your weight (kg): "))
    user_height = float(input("Please enter your height (cm): "))
    user_gender = input(
        "Please enter your gender (male/female): "
    ).lower()

    user_BMI = user_weight / ((user_height / 100) ** 2)

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("Height cannot be zero. Please enter a valid number.")

except Exception:
    print("Unknown error. Please try again later.")

else:
    print(f"Your BMI is {user_BMI:.2f}")

    if user_gender == "male":
        print("Mr.")
    elif user_gender == "female":
        print("Ms.")
    else:
        print("Invalid gender.")

    if user_BMI < 18.5:
        print("This BMI is classified as underweight.")
    elif user_BMI < 25.0:
        print("This BMI is classified as normal weight.")
    elif user_BMI < 30.0:
        print("This BMI is classified as overweight.")
    else:
        print("This BMI is classified as obesity.")

finally:
    print("Program has ended.")
