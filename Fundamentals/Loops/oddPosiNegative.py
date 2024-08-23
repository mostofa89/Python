a = 18
b = 63
for i in range (a, b+1, 9):
  if i<b:
    if i%2 == 0:
      print(i,end=", ")

    else:
      print(-i,end=", ")

  elif i == b:
    print(-i)