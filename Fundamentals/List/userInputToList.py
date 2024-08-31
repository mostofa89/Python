str1 : str  = input("Enter a Number : ")
nums : list = []
str2 : str = ""
for ch in str1:
    if ch == ",":
        nums.append(int(str2))
        str2 = ""

    elif ch == " ":
        continue

    else:
        str2 += ch


nums.append(int(str2))

print(nums)
