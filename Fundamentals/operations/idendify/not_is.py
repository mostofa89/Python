num1 = 6
num2 = 3
print(num1)  # Output: 6
print(num2)  # Output: 3
print(num1 is not num2)  # Output: True

num3 = 12.5
num4 = 4.0
print(num3)  # Output: 12.5
print(num4)  # Output: 4.0
print(num3 is not num4)  # Output: True

name1 = "HelloHello"
name2 = "HelloHello"
print(name1)  # Output: HelloHello
print(name2)  # Output: HelloHello
print(name1 is not name2)  # Output: False

is_active1 = True
is_active2 = False
print(is_active1) # Output: True
print(is_active2) # Output: False
print(is_active1 is not is_active2) # Output: False
is_active3 = True
print(is_active1 is not is_active3) # Output: True

list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
print(list1) # Output: [1, 2, 3, 4, 5, 6]
print(list2) # Output: [1, 2, 3, 4, 5, 6]
print(list1 is not list2) # Output: False
list3 = list1
print(list1 is not list3) # Output: True
print(list1 == list2) # Output: True

num5 = None
print(num5) # Output: None
print(num5 is not None) # Output: True

num6 = 0
print(num6) # Output: 0
print(num6 is not None) # Output: False
print(num6 is not 0) # Output: False
num7 = 0.0
print(num7) # Output: 0.0
print(num7 is not 0) # Output: False
print(num7 is not 0.0) # Output: True