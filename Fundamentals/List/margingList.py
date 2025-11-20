nums1 : list = [10, 20, 30, 40, 50]
nums2 : list = [60, 70, 80, 90, 100]

nums1 += nums2
print(nums1)


nums3 : list = [10, 20, 30, 40, 50]
nums4 : list = [60, 70, 80, 90, 100]

# Itterative way

for num in nums4:
    nums3.append(num)

print(nums3)