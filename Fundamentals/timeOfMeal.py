time = int(input("Enter the time : "))
if time > 3 and time < 7:
  print("Breakfast")

elif time > 11 and time < 14:
  print("Lunch")

elif time > 15 and time < 17:
  print("Snacks")

elif time > 18 and time < 21:
  print("Dinner")

elif time >= 0 and time <= 24:
  print("Patience is a virtue")

else:
  print("Wrong Time")