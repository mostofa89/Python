def calculate_sum(*nums):
    total = 0
    for num in nums:
        total += num

    print(f"The sum of the provided numbers is: {total}")


x = [10, 20, 30, 40, 50]

calculate_sum(*x)
calculate_sum(5, 15, 25)
