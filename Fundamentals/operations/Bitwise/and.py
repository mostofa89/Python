num1 = 5
num2 = 3
print(num1)  # Output: 5
print(num2)  # Output: 3
print(num1 & num2)  # Output: 1 (binary 0101 & 0011 = 0001)

num3 = 12
num4 = 5
print(num3)  # Output: 12
print(num4)  # Output: 5
print(num3 & num4)  # Output: 4 (binary 1100 & 0101 = 0100)

is_active1 = True
is_active2 = False
print(is_active1)  # Output: True
print(is_active2)  # Output: False
print(is_active1 & is_active2)  # Output: False (True & False = False)
is_active3 = True
print(is_active1 & is_active3)  # Output: True (True & True = True)

num5 = 0b1101  # binary for 13
num6 = 0b1011  # binary for 11
print(num5)  # Output: 13
print(num6)  # Output: 11
print(num5 & num6)  # Output: 9 (binary 1101 & 1011 = 1001)

num7 = 0b0000  # binary for 0
num8 = 0b1111  # binary for 15
print(num7)  # Output: 0
print(num8)  # Output: 15
print(num7 & num8)  # Output: 0 (binary 0000 & 1111 = 0000)

# Note: Bitwise AND operation is not supported for strings or lists in Python.
name1 = "Hello"
name2 = "World"
print(name1)  # Output: Hello
print(name2)  # Output: World
# print(name1 & name2)  # Output: Error (bitwise AND is not supported for strings)