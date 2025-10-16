num1 = 10
num2 = 20

sum = num1 + num2
print("The sum is:", sum) # Output: The sum is: 30

num3 = 15.5
num4 = 4.5
sum_float = num3 + num4
print("The sum of floats is:", sum_float) # Output: The sum of floats is: 20.0

# Adding strings (concatenation)
str1 = "Hello, "
str2 = "World!"
result_str = str1 + str2
print("The concatenated string is:", result_str) # Output: The concatenated string is: Hello, World!

# Adding lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = list1 + list2
print("The concatenated list is:", result_list) # Output: The concatenated list is: [1, 2, 3, 4, 5, 6] 

# Adding tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2
print("The concatenated tuple is:", result_tuple) # Output: The concatenated tuple is (1, 2, 3, 4, 5, 6)

# Adding dictionaries (merging)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result_dict = {**dict1, **dict2}
print("The merged dictionary is:", result_dict) # Output: The merged dictionary is: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Note: Adding incompatible types like int and str will raise a TypeError
# Uncommenting the following line will raise an error
# invalid_sum = num1 + str1
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Note: In Python, the '+' operator is used for addition and concatenation.
# It works with numbers, strings, lists, tuples, and dictionaries.
# However, adding incompatible types like int and str will raise a TypeError.
