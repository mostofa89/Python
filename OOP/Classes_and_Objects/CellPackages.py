class CellPackage:

    def __init__(self, price, data, talktime, mms_sms, discount, validity):
        self.price = price
        self.data = data
        self.talktime = talktime
        self.mms_sms = mms_sms
        self.discount = discount
        self.validity = validity


# Driver code to test the CellPackage class
pkg1=CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
print(f"Data = {int(pkg1.data[:-2])*1024} MB")
print(f"Talktime = {pkg1.talktime} talktime")
print(f"SMS/MMS = {pkg1.mms_sms}")
print(f"Validity = {pkg1.validity} Days")
print(f"--> Price = {pkg1.price} tk")
print(f"Buy now to get {int(pkg1.price*int(pkg1.discount[:-1])/100)} tk cashback.")


pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
print(f"Data = {int(pkg2.data[:-2])*1024} MB")
print(f"Talktime = {pkg2.talktime} talktime")
print(f"SMS/MMS = {pkg2.mms_sms}")
print(f"Validity = {pkg2.validity} Days")
print(f"--> Price = {pkg2.price} tk")
print(f"Buy now to get {int(pkg2.price*int(pkg2.discount[:-1])/100)} tk cashback.")


pkg3 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
print(f"Data = {int(pkg3.data[:-2])*1024} MB")
print(f"Talktime = {pkg3.talktime} talktime")
print(f"SMS/MMS = {pkg3.mms_sms}")
print(f"Validity = {pkg3.validity} Days")
print(f"--> Price = {pkg3.price} tk")
print(f"Buy now to get {int(pkg3.price*int(pkg3.discount[:-1])/100)} tk cashback.")
        