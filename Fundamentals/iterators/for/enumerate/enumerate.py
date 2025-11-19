words = "Python"
nums = [10, 20, 30, 40, 50]
tuple_nums = (100, 200, 300)

for index, letter in enumerate(words):
    print(f"Index: {index} Letter: {letter}")

for index, num in enumerate(nums):
    print(f"Index: {index} Number: {num}")

for index, tnum in enumerate(tuple_nums):
    print(f"Index: {index} Tuple Number: {tnum}")