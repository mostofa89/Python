class TaxiLagbe:
    def __init__(self, num, location="Dhaka"):
        self.taxi_number = num
        self.location = location
        self.total_fare = 0
        self.passengers_list = []


    def addPassenger(self, *passengers):
        for it in passengers:
            passenger, fare = it.split("_")
            if len(self.passengers_list) < 4:
                self.passengers_list.append(passenger.strip())
                self.total_fare += int(fare.strip())
                print(f"Dear {passenger}! Welcome to TaxiLagbe.")

            else:
                print("Taxi Full! No more passengers can be added.")


    def printDetails(self):
        print(f"""Trip info for Taxi number: {self.taxi_number}
This taxi can only cover the {self.location} area.
Total passengers: {len(self.passengers_list)}
Passenger lists:""")
        for i in range(len(self.passengers_list)):
            if i==len(self.passengers_list)-1:
                print(self.passengers_list[i])

            else:
                print(self.passengers_list[i], end=", ")

            print(f"Total collected fare: {self.total_fare} Taka")



taxi1 = TaxiLagbe("1010-01", "Dhaka")
print('-------------------------------')
taxi1.addPassenger('Walker_100','Wood_200','Matt_100')
taxi1.addPassenger("Wilson_105")
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()