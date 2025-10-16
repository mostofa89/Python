num1 = 10
num2 = 20

print(num1) # Output: 10
print(num2) # Output: 20

num2 -= num1
print(num2) # Output: 10

num3 = 4678.8997
num4 = 1234.5678
print(num3) # Output: 4678.8997
print(num4) # Output: 1234.5678

num4 -= num3
print(num4) # Output: -3444.3319

name1 = "John"
name2 = "Doe"
print(name1) # Output: John
print(name2) # Output: Doe
name2 = name1 + " " + name2
print(name2) # Output: John Doe
is_active1 = True
is_active2 = False
print(is_active1) # Output: True
print(is_active2) # Output: False
is_active2 -= is_active1
print(is_active2) # Output: -1 (False is treated as 0 and True as 1 in subtraction)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1) # Output: [1, 2, 3]
print(list2) # Output: [4, 5, 6]

list2 -= list1
print(list2) # Output: [4, 5, 6] (list subtraction is not supported, so list2 remains unchanged)
list1 = [2, 3]
list2 = [3, 4, 5]
