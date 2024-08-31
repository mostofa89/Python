nums : list = [4, 6, 9, 1, 31, 24]

print(nums[4])
print(nums[1 : len(nums)])
print(nums[0: len(nums) : 2])
print(nums[len(nums) - 1 : 0 : -2])

for i in range(len(nums)):
    print(nums[i])