str1 : str = "29837"
num : int = 76556
cgpa : float = 3.65
flag : bool = True
print(str1)
print(num)
print(cgpa)
print(flag)

num = int(str1)
str1 = str(num)
print("After Converting into Integer : ", num)
print("After Converting into String : ", str1)

num = int(cgpa)
cgpa = float(4)
num1 : int = int(flag)
print("After Converting into Integer : ", num)
print("After Converting into Float : ", cgpa)
print("After Converting into Integer : ", num1)