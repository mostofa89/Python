nums : list = [5, 3, 8, 1, 2]
sorted_nums = sorted(nums)
print("Original list:", nums)
print("Sorted list:", sorted_nums)

cars : list = ["BMW", "Audi", "Mercedes", "Toyota"]
sorted_cars = sorted(cars)
print("Original list:", cars)
print("Sorted list:", sorted_cars)

reversed_nums = sorted(nums, reverse=True)
print("Reversed sorted list:", reversed_nums)

reversed_cars = sorted(cars, reverse=True)
print("Reversed sorted list of cars:", reversed_cars)
