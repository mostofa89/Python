num1 = 10
num2 = 20

print(num1 >= num2)  # Output: False
print(num2 >= num1)  # Output: True

# You can also compare other data types like strings
str1 = "apple"
str2 = "banana"
print(str1 >= str2)  # Output: False
print(str2 >= str1)  # Output: True

# Comparison with floating-point numbers
float1 = 10.5
float2 = 10.0
print(float1 >= float2)  # Output: True
print(float2 >= float1)  # Output: False

# Comparison with equal values
print(num1 >= 10)  # Output: True
print(num2 >= 20)  # Output: True

# Comparison with negative numbers
neg1 = -5
neg2 = -10
print(neg1 >= neg2)  # Output: True
print(neg2 >= neg1)  # Output: False

# Comparison with zero
print(0 >= -1)  # Output: True
print(-1 >= 0)  # Output: False
print(0 >= 0)   # Output: True

# Comparison with mixed types (int and float)
print(10 >= 10.0)  # Output: True
print(10.5 >= 10)  # Output: True
print(10 >= 10.5)  # Output: False
print(10.0 >= 10.5)  # Output: False

# Note: Comparing incompatible types (like int and str) will raise a TypeError in Python 3
# Uncommenting the following line will raise an error
# print(10 >= "10")  # Raises TypeError
# Demonstrating the greater than or equal to (>=) operator in Python
# with various data types and scenarios.
