num1 = 10
num2 = 20
print(num1 == num2)  # Output: False
print(num2 == num1)  # Output: False

num3 = 23.8
num4 = 23.8
print(num3 == num4)  # Output: True
print(num3 == num1)  # Output: False

# You can also compare other data types like strings
str1 = "hello"
str2 = "hello"
print(str1 == str2)  # Output: True
str3 = "Hello"
print(str1 == str3)  # Output: False

# Comparison with mixed types (int and float)
print(num1 == 10.0)  # Output: True
print(num1 == 10.1)  # Output: False
print(num3 == 23)    # Output: False
print(num3 == 23.8)  # Output: True
print(num4 == 23.8)  # Output: True
print(num4 == 23.9)  # Output: False
# Note: Comparing incompatible types (like int and str) will raise a TypeError in Python 3
# Uncommenting the following line will raise an error
# print(10 == "10")  # Raises TypeError
# Demonstrating the equality (==) operator in Python
# with various data types and scenarios.
# to show how it works.
