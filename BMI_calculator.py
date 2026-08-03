#BMI calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:

    print("you are underweight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("overweight")
else:
    print("obese")


