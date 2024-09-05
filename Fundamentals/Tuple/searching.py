given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
counter = 0
val = int(input("Enter a Number : "))
for num in given_tuple:
  if val == num:
    counter += 1

  else:
    pass

print(val ,"appears,", counter, "times in the tuple")