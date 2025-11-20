nums : list = [1, 2, 3, 4, 5]
popped_element = nums.pop()
print("Original List:", [1, 2, 3, 4, 5])
print("Popped Element:", popped_element)
print("List after popping:", nums)

popped_element = nums.pop(1)
print("Popped Element at index 1:", popped_element)
print("List after popping at index 1:", nums)


fruits : list = ["apple", "banana", "cherry", "date"]
popped_fruit = fruits.pop()
print("Original Fruits List:", fruits)
print("Popped Fruit:", popped_fruit)
print("Fruits List after popping:", fruits)

popped_fruit = fruits.pop(len(fruits) - 2)
print("Popped Fruit at second last index:", popped_fruit)
print("Fruits List after popping second last element:", fruits)
