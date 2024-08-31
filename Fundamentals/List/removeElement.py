myList : list = ["hey", "there", "", "what's", "", "up", "", "?"]
newList = []

#Itterative way
for it in myList:
    if it == "":
        continue

    else:
        newList.append(it)

print(newList)

# Using Built in

myList.remove("")
print(newList)