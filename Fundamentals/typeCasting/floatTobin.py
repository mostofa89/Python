num1 = 1.0
num2 = 0.0

bool_num1 = bool(int(num1))
bool_num2 = bool(int(num2))

print(f"Binary representation of {num1}: {bool_num1}")  # Output: True
print(f"Binary representation of {num2}: {bool_num2}")  # Output: False
print(f"Type of num1: {type(num1)}")        # Output: <class 'float'>
print(f"Type of num2: {type(num2)}")        # Output: <class 'float'>
print(f"Type of bool_num1: {type(bool_num1)}")  # Output: <class 'bool'>
print(f"Type of bool_num2: {type(bool_num2)}")  # Output: <class 'bool'>
print(f"Value of num1: {num1}")              # Output: 1.0
print(f"Value of num2: {num2}")              # Output: 0.0
print(f"Value of bool_num1: {bool_num1}")      # Output: True
print(f"Value of bool_num2: {bool_num2}")      # Output: False
print(f"Concatenation of bool_num1 and bool_num2: {bool_num1 + bool_num2}")  # Output: 1
