class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            print(f"{amount} deposited. Balance = {self.balance}")
        except ValueError as e:
            print("Error:", e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdraw amount must be positive")
            if amount > self.balance:
                raise ValueError("Not enough balance")
            self.balance -= amount
            print(f"{amount} withdrawn. Balance = {self.balance}")
        except ValueError as e:
            print("Error:", e)

    def check_balance(self):
        print(f"Current Balance = {self.balance}")
print(" Welcome to Bank System ")
name = input("Enter your name: ")
account = BankAccount(name, 10000)   # Starting with 1000 balance
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        try:
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        try:
            amt = float(input("Enter withdraw amount: "))
            account.withdraw(amt)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for using our Bank System! Goodbye")
        break
    else:
        print("Invalid choice! Please select 1–4.")

