num : int = int(input("Enter a Number : "))

while num > 0:
    mod = num % 10
    num //= 10
    if num == 0:
        print(mod)

    else:
        print(mod, end = ", ")