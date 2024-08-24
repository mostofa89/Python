num : int = int(input("Enter a Number : "))
counter : int = 0

while num > 0:
    num //= 10
    counter += 1


print(counter)