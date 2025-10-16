nums = [1, 2, 3, 4, 5]
print(nums)  # Output: [1, 2, 3, 4, 5]
print(3 in nums)  # Output: True
print(6 in nums)  # Output: False

name = "HelloWorld"
print(name)  # Output: HelloWorld
print('H' in name)  # Output: True
print('h' in name)  # Output: False
chars = {'a', 'b', 'c', 'd'}
print(chars)  # Output: {'a', 'b', 'c', 'd'}
print('a' in chars)  # Output: True
print('z' in chars)  # Output: False
person = {'name': 'Alice', 'age': 30}
print(person)  # Output: {'name': 'Alice', 'age': 30}
print('name' in person)  # Output: True
print('Alice' in person)  # Output: False

num = None
print(num)  # Output: None
print(num in nums)  # Output: False

num = 3
print(num)  # Output: 3
print(num in nums)  # Output: True