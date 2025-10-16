num = 100
str_num = str(num)

print(f"Type of num: {type(num)}")        # Output: <class 'int'>
print(f"Type of str_num: {type(str_num)}")  # Output: <class 'str'>
print(f"Value of num: {num}")              # Output: 100
print(f"Value of str_num: {str_num}")      # Output: "100"
print(f"Concatenation of str_num and ' is a string': {str_num + ' is a string'}")  # Output: "100 is a string"
print(f"Sum of num and 50: {num + 50}")    # Output: 150