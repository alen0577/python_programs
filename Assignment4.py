def bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi


weight = float(input("Enter your weight in Kg "))
height = float(input("Enter your height in cm "))
bmi = bmi(weight, height)
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("Below Normal weight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")
