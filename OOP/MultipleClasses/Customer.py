class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)


    def show_accounts(self):
        print(f"Customer: {self.name}")
        print("Accounts:")
        for acc in self.accounts:
            print(f"{acc.account_type}: ${acc.balance}")

        print("====================================")


class Account:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []


    def add_customer(self, customer):
        self.customers.append(customer)


    def show_all_customers(self):
        print(f"\nBank: {self.name}")
        for c in self.customers:
            c.show_accounts()


# Driver code
bank = Bank("Sonali Bank")
c1 = Customer("Joy")
a1 = Account("Savings", 20000)
a2 = Account("Checking", 5000)

c1.add_account(a1)
c1.add_account(a2)

bank.add_customer(c1)
bank.show_all_customers()
