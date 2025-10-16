num1 = 6
num2 = 3
print(num1) # Output: 6
print(num2) # Output: 3
print(num1 is num2) # Output: False

num3 = 12.5
num4 = 4.0
print(num3) # Output: 12.5
print(num4) # Output: 4.0
print(num3 is num4) # Output: False

name1 = "HelloHello"
name2 = "HelloHello"
print(name1) # Output: HelloHello
print(name2) # Output: HelloHello
print(name1 is name2) # Output: True

is_active1 = True
is_active2 = False
print(is_active1) # Output: True
print(is_active2) # Output: False
print(is_active1 is is_active2) # Output: False
is_active3 = True
print(is_active1 is is_active3) # Output: True

list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
print(list1) # Output: [1, 2, 3, 4, 5, 6]
print(list2) # Output: [1, 2, 3, 4, 5, 6]
print(list1 is list2) # Output: False
list3 = list1
print(list1 is list3) # Output: True
print(list1 == list2) # Output: True

num5 = None
print(num5) # Output: None
print(num5 is None) # Output: True

num6 = 0
print(num6) # Output: 0
print(num6 is None) # Output: False
print(num6 is 0) # Output: True
num7 = 0.0
print(num7) # Output: 0.0
print(num7 is 0) # Output: False
print(num7 is 0.0) # Output: True