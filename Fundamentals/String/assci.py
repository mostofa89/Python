str1 : str = input("Enter a String : ")

for i in range(len(str1)):
    print(f"{str1[i]} : {ord(str1[i])}")