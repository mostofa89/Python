num1 = 6
num2 = 3
print(num1) # Output: 6
print(num2) # Output: 3
num1 /= num2
print(num1) # Output: 2.0

num3 = 12.5
num4 = 4.0
print(num3) # Output: 12.5
print(num4) # Output: 4.0
num3 /= num4
print(num3) # Output: 3.125

name1 = "HelloHello"
name2 = 3
print(name1) # Output: HelloHello
print(name2) # Output: 3
# name1 /= name2
# print(name1) # Output: Error (string division is not supported)

is_active1 = True
is_active2 = False
print(is_active1) # Output: True
print(is_active2) # Output: False
# is_active1 /= is_active2
print(is_active1) # Output: Error (division by zero)

list1 = [1, 2, 3, 4, 5, 6]
num1 = 2
print(list1) # Output: [1, 2, 3, 4, 5, 6]
print(num1) # Output: 2
# list1 /= num1
# print(list1) # Output: Error (list division is not supported)
