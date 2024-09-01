my_list = [10, -1, -10, 100, 10, -1]
max_num = None
max_idx = 0
min_idx = 0
min_num = None
for i in range(len(my_list)):
  if max_num == None:
    max_num = my_list[i]
    min_num = my_list[i]

  if my_list[i] > max_num:
    max_num = my_list[i]
    max_idx = i

  if my_list[i] < min_num:
    min_num = my_list[i]
    min_idx = i


print("Largest number in the list is "+ str(max_num) + ". which was found at index" + str(max_idx) + ".")
print("Smallest number in the list is "+ str(min_num) + ". which was found at index" + str(min_idx) + ".")