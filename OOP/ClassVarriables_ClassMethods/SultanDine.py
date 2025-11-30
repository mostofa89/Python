class SultansDine:
    branch_count = 0
    branch_info = []
    sell = 0

    def __init__(self, branch):
        self.branch = branch
        self.sell = 0
        SultansDine.branch_count += 1
        SultansDine.branch_info.append(branch)


    @classmethod
    def details(cls):
        if SultansDine.sell == 0:
            print(f"""Total Number of branch(s): {SultansDine.branch_count}
Total Sell: {SultansDine.sell} Taka""")

        else:
            print(f"""Total Number of branch(s): {SultansDine.branch_count}
Total Sell: {SultansDine.sell} Taka""")
            for i in range(0, len(SultansDine.branch_info) - 1, 2):
                print(f"""Branch Name: {SultansDine.branch_info[i]}, Branch Sell: {SultansDine.branch_info[i+1]} Taka
Branch consists of total sell's: {((SultansDine.branch_info[i+1] / SultansDine.sell) * 100):.2f}%""")

    def sellQuantity(self, quantity):
        if quantity < 10:
            self.sell += quantity*300

        elif quantity < 20:
            self.sell += quantity * 350

        else:
            self.sell += quantity * 400

        SultansDine.sell += self.sell
        SultansDine.branch_info.append(self.sell)



    def branchInformation(self):
        print(f"""Branch Name: {self.branch}
Branch Sell: {self.sell} Taka""")



SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()