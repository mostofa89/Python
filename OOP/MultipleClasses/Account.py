class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount


class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
        else:
            print("Insufficient balance!")


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


# Driver Code
print("====================================")
b = Bank("BRAC Bank")
c = Customer("Joy")
acc = Account("12345")

c.add_account(acc)
b.add_customer(c)

acc.deposit(20000)
acc.withdraw(5000)

print(c.name, "Account Balance:", acc.balance)
print("Transactions:")
for t in acc.transactions:
    print(f"- {t.type}: ${t.amount}")

print("====================================")