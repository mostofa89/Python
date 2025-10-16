num1 = 2
num2 = 3
print(num1) # Output: 2
print(num2) # Output: 3

num1 *= num2
print(num1) # Output: 6

num3 = 12.5
num4 = 4.0
print(num3) # Output: 12.5
print(num4) # Output: 4.0
num3 *= num4
print(num3) # Output: 50.0

name1 = "Hello"
name2 = "World"
print(name1) # Output: Hello
print(name2) # Output: World

name1 *= 3
print(name1) # Output: HelloHelloHello
is_active1 = True
is_active2 = False
print(is_active1) # Output: True
print(is_active2) # Output: False

is_active1 *= is_active2
print(is_active1) # Output: 0 (True is treated as 1 and False as 0 in multiplication)
list1 = [1, 2]
list2 = [3, 4]
print(list1) # Output: [1, 2]
print(list2) # Output: [3, 4]
list1 *= 2

print(list1) # Output: [1, 2, 1, 2]
list2 *= 3
print(list2) # Output: [3, 4, 3, 4, 3, 4]
dict1 = {"a": 1}
dict2 = {"b": 2}

print(dict1) # Output: {'a': 1}
print(dict2) # Output: {'b': 2}

print(dict1) # Output: {'a': 1}
set1 = {1, 2}
set2 = {3, 4}
print(set1) # Output: {1, 2}
print(set2) # Output: {3, 4}
set1 *= 2
print(set1) # Output: {1, 2} (set multiplication is not supported, so set1 remains unchanged)
set2 *= 3
print(set2) # Output: {3, 4} (set multiplication is not supported, so set2 remains unchanged)
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1) # Output: (1, 2)
print(tuple2) # Output: (3, 4)
tuple1 *= 2