#BMI convertor
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

BMI = ((weight) / height ** 2)*10000
print(f"your BMI is {round(BMI, 2)}")

if BMI < 18.5:
    print("you are underweight")
elif 18.5 <= BMI <= 24.9:
    print("you hve a normal weight")
elif 25 <= BMI <= 29.9:
    print("you are overweight")
elif BMI >= 30:
    print("you are obese")
else:
    print("Invalid")