class KK_tea:
    sales = {'KK Regular Tea': 0}

    def __init__(self, price, tea_bags=50):
        self.price = price
        self.tea_bags = tea_bags
        self.status = False
        self.weight = self.tea_bags * 2


    @classmethod
    def update_sold_status_regular(cls, *teas):
        for tea in teas:
            tea.status = True
            KK_tea.sales["KK Regular Tea"] += 1


    def product_detail(self):
        print(f"""Name: KK Regular Tea, Weight: {self.weight}
Tea Bags: {self.tea_bags}, Price: {self.price}
Status: {self.status}""")


    @classmethod
    def total_sales(cls):
        print(f"Total sales: {KK_tea.sales}")


class KK_flavoured_tea(KK_tea):
    def __init__(self, flavour, price, tea_bags):
        self.flavour = flavour
        super().__init__(price, tea_bags)


    @classmethod
    def update_sold_status_flavoured(cls, *teas):
        for tea in teas:
            tea.status = True
            if tea.flavour in KK_tea.sales:
                KK_tea.sales[tea.flavour] += 1
            else:
                KK_tea.sales[tea.flavour] = 1


    def product_detail(self):
        print(f"""Name: {self.flavour} Flavoured Tea, Weight: {self.weight}
Tea Bags: {self.tea_bags}, Price: {self.price}
Status: {self.status}""")


# ===========================================================
# MULTIPLE INHERITANCE (Using a separate Mixin)
# ===========================================================
class FlavourMixin:
    def __init__(self, flavour):
        self.flavour = flavour


    def update_flavoured_sale(self):
        if self.flavour in KK_tea.sales:
            KK_tea.sales[self.flavour] += 1
        else:
            KK_tea.sales[self.flavour] = 1


class KK_SpecialTea(KK_tea, FlavourMixin):
    def __init__(self, flavour, price, tea_bags=50):
        KK_tea.__init__(self, price, tea_bags)
        FlavourMixin.__init__(self, flavour)


    def special_detail(self):
        print(f"Special Tea: {self.flavour}, Weight: {self.weight}, Price: {self.price}, Status: {self.status}")



# ===========================================================
# DRIVER CODE
# ===========================================================
# Regular tea
t1 = KK_tea(250)
t2 = KK_tea(300, 60)
KK_tea.update_sold_status_regular(t1, t2)

print("========== Regular Tea Details ==========")
t1.product_detail()
t2.product_detail()
KK_tea.total_sales()
print("========================================\n")

# Flavoured tea
t3 = KK_flavoured_tea("Jasmine", 260, 50)
t4 = KK_flavoured_tea("Honey Lemon", 270, 45)
KK_flavoured_tea.update_sold_status_flavoured(t3, t4)

print("========= Flavoured Tea Details =========")
t3.product_detail()
t4.product_detail()
KK_tea.total_sales()
print("========================================\n")

# Special Tea
t5 = KK_SpecialTea("Mint", 280, 40)
t5.special_detail()
t5.update_flavoured_sale()
t5.product_detail()

print("=========== Total Sales ================")
KK_tea.total_sales()
print("========================================")


