num1 = 10
num2 = 20
print(num1) # Output: 10
print(num2) # Output: 20

num1 += num2
print(num1) # Output: 30

num3 = 4678.8997
num4 = 1234.5678
print(num3) # Output: 4678.8997
print(num4) # Output: 1234.5678

num3 += num4
print(num3) # Output: 5913.4675

name1 = "John"
name2 = "Doe"
print(name1) # Output: John
print(name2) # Output: Doe

name1 += " " + name2
print(name1) # Output: John Doe

is_active1 = True
is_active2 = False
print(is_active1) # Output: True
print(is_active2) # Output: False
is_active1 += is_active2
print(is_active1) # Output: 1 (True is treated as 1 in addition

is_active2 += True
print(is_active2) # Output: 1 (False is treated as 0 in addition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1) # Output: [1, 2, 3]

print(list2) # Output: [4, 5, 6]
list1 += list2
print(list1) # Output: [1, 2, 3, 4, 5, 6]

list2 += [7, 8, 9]
print(list2) # Output: [4, 5, 6, 7, 8, 9]

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(dict1) # Output: {'a': 1, 'b': 2}
print(dict2) # Output: {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2.update({"e": 5, "f": 6})

print(dict2) # Output: {'c': 3, 'd': 4, 'e': 5, 'f': 6}
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1) # Output: {1, 2, 3}
print(set2) # Output: {4, 5, 6}
set1 |= set2
print(set1) # Output: {1, 2, 3, 4, 5, 6}
set2 |= {7, 8, 9}
print(set2) # Output: {4, 5, 6, 7, 8, 9}

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1) # Output: (1, 2, 3)
print(tuple2) # Output: (4, 5, 6)

tuple1 += tuple2
print(tuple1) # Output: (1, 2, 3, 4, 5, 6)
tuple2 += (7, 8, 9)
print(tuple2) # Output: (4, 5, 6, 7, 8, 9)