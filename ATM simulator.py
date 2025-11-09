# ATM withdrawal
def atm_withdrawal():
    saving = 1000
    print("your current balance is 1000$")
    balance = float(input("Enter your withdrawal money : "))
    if balance > saving:
        print("you have insufficient savings!")
    elif balance == saving:
        print("your current saving is 0$")
    elif balance < saving:
        print(f"your saving is {saving - balance}$")
    else:
        print("Invalid")
        
atm_withdrawal()
        