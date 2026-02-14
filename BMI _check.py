weight = float(input("enter your weight (kg): "))
height = float(input("enter your height (m): "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")