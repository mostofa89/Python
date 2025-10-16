num1 = 10
num2 = 20
print(num1 == num2)  # Output: False
print(num2 == num1)  # Output: False

# You can also compare other data types like strings
str1 = "hello"
str2 = "hello"
print(str1 != str2)  # Output: False
str3 = "Hello"
print(str1 != str3)  # Output: True

# Comparison with mixed types (int and float)
print(num1 != 10.0)  # Output: False
print(num1 != 10.1)  # Output: True
print(num1 != 20)    # Output: True
print(num2 != 20)    # Output: False
print(num2 != 20.0)  # Output: False
print(num2 != 20.1)  # Output: True
print(num1 != num2)  # Output: True
print(num2 != num1)  # Output: True
print(num1 != 15)    # Output: True
print(num2 != 15)    # Output: True
print(num1 != 10)    # Output: False
print(num2 != 25)    # Output: True
print(num1 != 5)     # Output: True
print(num2 != 30)    # Output: True
print(num1 != -10)   # Output: True
print(num2 != -20)   # Output: True
print(num1 != 0)     # Output: True
print(num2 != 0)     # Output: True
print(num1 != -5)    # Output: True
print(num2 != -15)   # Output: True

# Note: Comparing incompatible types (like int and str) will raise a TypeError in Python 3
# Uncommenting the following line will raise an error
# print(10 != "10")  # Raises TypeError
# Demonstrating the not equal to (!=) operator in Python
# with various data types and scenarios.