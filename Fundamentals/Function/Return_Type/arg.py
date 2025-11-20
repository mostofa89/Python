def calculate_sum(*nums):
    total = 0
    for num in nums:
        total += num

    return f"The sum of the provided numbers is: {total}"


x = [10, 20, 30, 40, 50]

print(calculate_sum(*x))
print(calculate_sum(5, 15, 25))