num1 = 5
num2 = 3
print(num1)  # Output: 5
print(num2)  # Output: 3
print(num1 | num2)  # Output: 7 (binary 0101 | 0011 = 0111)

num3 = 12
num4 = 5
print(num3)  # Output: 12
print(num4)  # Output: 5
print(num3 | num4)  # Output: 13 (binary 1100 | 0101 = 1101)

is_active1 = True
is_active2 = False
print(is_active1)  # Output: True
print(is_active2)  # Output: False
print(is_active1 | is_active2)  # Output: True (True | False = True)
is_active3 = True
print(is_active1 | is_active3)  # Output: True (True | True = True)


num5 = 0b1101  # binary for 13
num6 = 0b1011  # binary for 11
print(num5)  # Output: 13
print(num6)  # Output: 11
print(num5 | num6)  # Output: 15 (binary 1101 | 1011 = 1111)

str1 = "Hello"
str2 = "World"
print(str1)  # Output: Hello
print(str2)  # Output: World
# print(str1 | str2)  # Output: Error (bitwise OR is not supported for strings)

num1_float = 5.5
num2_float = 3.3
print(num1_float)  # Output: 5.5
print(num2_float)  # Output: 3.3
# print(num1_float | num2_float)  # Output: Error (bitwise OR is not supported for floats) 