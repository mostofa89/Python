# Parent class
from typing import override


class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn: ${amount}. New balance: ${self.balance}"
        return "Insufficient funds!"
    

    def get_account_type(self):
        return "Generic Account"


# Child class 1 - Savings Account with withdrawal limit
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.withdrawal_limit = 500
    

    @override
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"Withdrawal limit exceeded! Max: ${self.withdrawal_limit}"
        return super().withdraw(amount)  # Call parent's withdraw
    

    def get_account_type(self):
        return "Savings Account"


# Child class 2 - Current Account with overdraft
class CurrentAccount(BankAccount):

    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    

    @override
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrawn: ${amount}. Balance: ${self.balance}"
        return f"Exceeds overdraft limit of ${self.overdraft_limit}!"
    

    def get_account_type(self):
        return "Current Account"


# Testing
print("=== Bank Account Method Overriding ===\n")

# Create accounts
savings = SavingsAccount("SAV001", 1000)
current = CurrentAccount("CUR001", 500, 200)

# Test overridden methods
print(f"Account Type: {savings.get_account_type()}")
print(savings.withdraw(300))   # Success
print(savings.withdraw(600))   # Exceeds withdrawal limit
print()

print(f"Account Type: {current.get_account_type()}")
print(current.withdraw(600))   # Uses overdraft
print(current.withdraw(200))   # Exceeds overdraft limit