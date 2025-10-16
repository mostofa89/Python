num1 = 10
num2 = 20

print(num1 and num2)  # Output: 20

# Logical AND with boolean values
bool1 = True
bool2 = False
print(bool1 and bool2)  # Output: False
print(bool1 and True)   # Output: True
print(bool2 and False)  # Output: False
print(bool1 and False)  # Output: False
print(bool2 and True)   # Output: False

# Logical AND with mixed types
print(num1 and bool1)  # Output: True
print(num2 and bool2)  # Output: False
print(bool1 and num1)  # Output: 10
print(bool2 and num2)  # Output: False
print(num1 and 0)      # Output: 0
print(num2 and 15)     # Output: 15
print(0 and num1)      # Output: 0
print(15 and num2)     # Output: 20
 
# Logical AND with strings
str1 = "hello"
str2 = "world"
print(str1 and str2)  # Output: world
print(str1 and "")     # Output: (empty string)
print("" and str2)     # Output: (empty string)
print("" and "")       # Output: (empty string)
print(str1 and True)   # Output: True
print(str2 and False)  # Output: False
print(True and str1)   # Output: hello
print(False and str2)  # Output: False

# Note: In Python, the 'and' operator returns the first falsy value or the last value if all are truthy.
# Demonstrating the logical AND (and) operator in Python
# with various data types and scenarios.