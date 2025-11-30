class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_cost(self):
        return self.product.price * self.quantity


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, order_item):
        self.items.append(order_item)

    def total_cost(self):
        return sum(item.get_cost() for item in self.items)


class Customer:
    def __init__(self, name):
        self.name = name

    def place_order(self, order):
        print(f"{self.name}'s Order Summary:")
        for item in order.items:
            print(f"- {item.product.name} x{item.quantity}")
        print("Total:", order.total_cost(), "Tk")


# Driver code
print("====================================")
cust = Customer("Joy")
p1 = Product("Laptop", 80000)
p2 = Product("Mouse", 800)

order = Order(cust)
order.add_item(OrderItem(p1, 1))
order.add_item(OrderItem(p2, 2))

cust.place_order(order)
print("====================================")