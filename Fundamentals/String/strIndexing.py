str1 : str = "Hello World"
print(str1[6])


for i in range(len(str1)):
    if len(str1) - 1 == i:
        print(str1[i])

    else:
        print(str1[i], end = ", ")
