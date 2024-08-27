Flag : bool = True
str1 : str = input("Enter a Number : ")
for i in  range(0, len(str1)):
  if str1[i] != "0" and str1[i] != "1":
    Flag = False

  else:
    pass
if Flag == True:
  print("Binary Number")

else:
  print("Not a Binary Number")