# tax convertor

income = int(input("Enter your income : "))

while income >= 0:
    if 0 <= income <= 2000:
        print(f"you are free from this year's tax👍")
    elif 2000 < income <= 4000:
        print(f"your tax is : {income * 15/100}")
    elif 4000 < income <= 7000:
        print(f"your tax is : {income * 20/100}")
    elif 7000 < income <= 10000:
        print(f"your tax is : {income * 25/100}")
    elif 10000 < income <= 14000:
        print(f"your tax is : {income * 30/100}")
    elif income > 14000:
        print(f"your tax is : {income * 35/100 }")
    else:
        print("Invalid")

    
