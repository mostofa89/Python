str1 = "Hello World"
index = str1.index("World")
print("The index of 'World' in the string is:", index)
print("The index of 'W' is:", str1.index("W"))


counter = 0
for char in str1:
    if char == "W":
        print("Found 'W' at index:", counter)
        break

    counter += 1