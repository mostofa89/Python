str1 : str = input("Enter a String : ")
str2 : str = ""
for ch in str1:
    if ch not in str2:
        str2 += ch

print(str2)