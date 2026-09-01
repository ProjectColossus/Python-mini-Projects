class Bank:

    def __init__(self):
        self.balance = 0
        self.pin = ""
        print("Welcome to Banking Centre")
        self.menu()

    def menu(self):
        user_input = int(input("""
                      Hello How would you Like to Proceed?
                      1. Enter 1 - Create a Pin.
                      2. Enter 2 - to Deposit
                      3. Enter 3 - to withdraw
                      4. Enter 4 - check balance
                      5. Enter 5 - Exit
                       
                        Enter your Choice """))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        else:
            print("Bye")
        
        
    def create_pin(self):
        self.pin = int(input("Enter your Pin: "))
        print("PIN Set Successfully!")

    def deposit(self):
        a = int(input("Enter your PIN: "))
        if a == self.pin:
            amount = int(input("Enter the Amount to Deposit: "))
            self.balance += amount
            print("Deposit Done Successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        a = int(input("Enter your PIN: "))
        if a == self.pin:
            amount = int(input("Enter the amount to Withdraw: "))
            if amount < self.balance:
                self.balance -= amount 
                print("Withdrawn Successfully")
            else:
                print("Insufficent Balance")
        else:
            print("Invalid PIN")

    def check_balance(self):
        a = int(input("Enter your PIN: "))
        if a == self.pin:
            print(f"Your Available Balance:{self.balance}")
        else:
            print("Invalid PIN")


sbi = Bank()
print(sbi.pin)
sbi.deposit()
sbi.withdraw()
sbi.check_balance()
