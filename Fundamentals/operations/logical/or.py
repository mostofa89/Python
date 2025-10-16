num1 = 10
num2 = 20
print(num1 or num2)  # Output: 10

num1 = 1.099
num2 = 20.99
print(num1 or num2)  # Output: 1.099

num1 = ""
num2 = "Hello"
print(num1 or num2)  # Output: Hello

num1 = None
num2 = "World"
print(num1 or num2)  # Output: World

num1 = []
num2 = [1, 2, 3]
print(num1 or num2)  # Output: [1, 2, 3]

num1 = False
num2 = True
print(num1 or num2)  # Output: True

num1 = 0
num2 = 42
print(num1 or num2)  # Output: 42

num1 = {}
num2 = {"key": "value"}
print(num1 or num2)  # Output: {'key': 'value'}

num1 = set()
num2 = {1, 2, 3}
print(num1 or num2)  # Output: {1, 2, 3}

num1 = ()
num2 = (4, 5, 6)
print(num1 or num2)  # Output: (4, 5, 6)

num1 = 0.0
num2 = 3.14
print(num1 or num2)  # Output: 3.14