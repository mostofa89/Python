num : int = int(input("Enter a Number : "))
counter : int = 0
n : int = num

while n > 0:
    n //= 10
    counter += 1


div : int = 10 ** (counter - 1)
while counter > 0:
    ans : int = num // div
    num %= div
    div //= 10
    if counter == 1:
        print(ans)

    else:
        print(ans, end = ", ")

    counter -= 1