class ATM:
    def __init__(self, balance):
        self.__balance = balance


    def __verify_pin(self, pin):
        return pin == "1234"


    def withdraw(self, amount, pin):
        if self.__verify_pin(pin) == True:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} withdrawn. New balance: {self.__balance}")
                

            else:
                print("Insufficient balance")

        else:
            print("Invalid PIN")




# Driver code
atm = ATM(1000)
print("====================================")
atm.withdraw(500, "1234")
print("====================================")
atm.withdraw(500, "123")
print("====================================")
atm.withdraw(1500, "1234")
print("====================================")