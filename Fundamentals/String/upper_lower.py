str1 : str = input("Enter a String : ")
upper_str : str = ""
lower_str : str = ""
for i in range(len(str1)-1, -1, -1):
    upper_str = str1[i].upper() + upper_str
    lower_str = str1[i].lower() + lower_str
    
print("Uppercase characters (reversed):", upper_str)
print("Lowercase characters (reversed):", lower_str)