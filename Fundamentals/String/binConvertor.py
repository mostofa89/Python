num : int = int(input("Enter a Number : "))
binNum : str = ""
while num > 0:
    num1 : int = num % 2
    num //= 2

    binNum = str(num1) + binNum

print(binNum)