age = int(input("Enter your age: "))

if 0 < age <= 12:
    print("Child")
elif 13 < age <= 17:
    print("Teenager")
elif 18 < age <= 64:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print('Invalid age')