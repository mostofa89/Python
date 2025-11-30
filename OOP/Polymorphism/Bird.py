class Bird:

    def fly(self):
        print("Bird can fly")


class Airplane:

    def fly(self):
        print("Airplane can fly")


def lets_fly(flyable):
    flyable.fly()


b = Bird()
a = Airplane()
lets_fly(b)
lets_fly(a)
