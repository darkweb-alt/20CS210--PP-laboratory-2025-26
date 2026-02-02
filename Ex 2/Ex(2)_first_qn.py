# ===============================
# Exercise 1: Bank Account System
# ===============================

# Base class
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        # Public data member
        self.account_holder = account_holder
        
        # Private data member (Encapsulation)
        self.__balance = initial_balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{self.__balance}")
        else:
            print("Error: Insufficient balance.")

    # Getter method to access private balance
    def get_balance(self):
        return self.__balance


# Subclass SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        # Call base class constructor
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    # Overriding withdraw method (Polymorphism)
    def withdraw(self, amount):
        if amount > 20000:
            print("Error: Maximum withdrawal limit is ₹20,000 per transaction.")
        else:
            super().withdraw(amount)

    # Method to add interest
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ₹{interest:.2f} added.")


# ===============================
# Testing Exercise 1
# ===============================

print("\n--- BankAccount Testing ---")
acc1 = BankAccount("Pitambar", 50000)
acc1.deposit(10000)
acc1.withdraw(15000)
print("Final Balance:", acc1.get_balance())

print("\n--- SavingsAccount Testing ---")
sav1 = SavingsAccount("Pitambar", 80000, 5)
sav1.withdraw(25000)      # Should fail due to limit
sav1.withdraw(15000)      # Should succeed
sav1.add_interest()
print("Final Balance:", sav1.get_balance())
