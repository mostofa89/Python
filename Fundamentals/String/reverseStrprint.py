str : str = input("Enter a String : ")
for i in range(len(str)-1, -1, -1):
  print(str[i], end = "")