
#deep Copying a list in Python using the copy() method
nums : list = [1, 2, 3, 4, 5]
copied_nums = nums.copy()
print("Original list:", nums)
print("Copied list:", copied_nums)

copied_nums.append(6)
print("After appending to copied list:")
print("Original list:", nums)
print("Copied list:", copied_nums)

bikes : list = ["Yamaha", "Suzuki", "Kawasaki"]
copied_bikes = bikes[:: 1]
print("Original list of bikes:", bikes)
print("Copied list of bikes:", copied_bikes)
copied_bikes.append("Ducati")
print("After appending to copied list of bikes:")
print("Original list of bikes:", bikes)
print("Copied list of bikes:", copied_bikes)


#Shallow Copying a list in Python by assignment
cars : list = ["Toyota", "Honda", "Ford"]
copied_cars = cars
print("Original list of cars:", cars)
print("Copied list of cars (reference):", copied_cars)
copied_cars.append("Chevrolet")
print("After appending to copied list (reference):")
print("Original list of cars:", cars)
print("Copied list of cars (reference):", copied_cars)