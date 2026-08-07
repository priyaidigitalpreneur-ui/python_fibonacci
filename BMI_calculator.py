class BMICalculator:

    def get_data(self):
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        return weight, height

    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

    def display_result(self, bmi):
        print(f"Your BMI is {bmi:.2f}")


calculator = BMICalculator()

weight, height = calculator.get_data()
bmi = calculator.calculate_bmi(weight, height)
calculator.display_result(bmi)