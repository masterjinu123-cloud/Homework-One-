 #unit conerter from celsius to fahrenheit or meter to feet

def tempcon():
    temprature = float(input("Enter the temprature : "))
    unit = input("Celsius or Fahrenheit? (C or F) : ")
    if unit == "C":
        temprature = (temprature * 9/5) + 32
        unit == "Fahrenheit"
    elif unit == "F":
        temprature = (temprature - 32) / 1.8
        unit == "Celsius"
    else:
        print(f"{unit} was not valid")
    print(f"The temprature is {temprature} {unit}")

def meterconv():
    length = float(input("Enter the length : "))
    unit = input("Meter or Feet? (M or F) : ")
    if unit == "M":
        length = length * 3.281
        unit == "Feet"
    elif unit == "F":
        length = length / 3.281
        unit == "Meter"
    else:
        print(f"{unit} was not valid")
    print(f"The length is {length} {unit}")


choice = int(input("Enter 1 to activate temprature convertion or press 2 to activate length converstion : "))

if choice == 1:
    tempcon()
elif choice == 2:
    meterconv()
    
