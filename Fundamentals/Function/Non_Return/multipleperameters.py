def greet(name, age):
    print(f"Hello, {name}, you are {age} years old, welcome to the program!")


print("Enter your name:", end=" ")
user_name = input()
print("Enter your age:", end=" ")
user_age = input()
greet(user_name, user_age)