str1 : str = input("Enter a String : ")
counter : int = 0
str2 : str = ""
for i in range(len(str1)):
  if str1[i] == " ":
    counter += 1

  if counter %2 == 0:
    if i%2 == 0 and ord(str1[i])>= 97 and ord(str1[i]) <= 122:
      str2 += chr(ord(str1[i])-32)

    else:
      str2 += str1[i]

  elif counter%2 != 0:
    if i%2 != 0 and ord(str1[i]) >= 97 and ord(str1[i]) <= 122:
      str2 += chr(ord(str1[i])-32)

    else:
      str2 += str1[i]

  else:
    pass

print(str2)