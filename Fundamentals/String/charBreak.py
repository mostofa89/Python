str1 : str = input("Enter a String : ")
char : str = input("Enter a char : ")
str2 = ""

for ch in str1:
  if ch == char:
    print(str2)
    str1=""

  else:
    str2 += ch

print(str2)