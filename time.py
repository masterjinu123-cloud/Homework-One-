hour = int(input('Time: '))

if 5 <= hour <= 11:
    print("Morning")
elif 12 <= hour <= 16:
    print("Afternoon")
elif 17 <= hour <= 20:
    print("Evening")
elif 21 <= hour <= 23:
    print("Night")
elif 0 <= hour <= 4:
    print("Night")
else:
    print("invalid")