str1 = "   Hello World   "
stripped_str = str1.strip()
print("The original string is:", repr(str1))
print("The stripped string is:", stripped_str)


# Manual strip implementation
start = 0
end = len(str1) - 1
while start <= end and str1[start] == " ":
    start += 1

while end >= start and str1[end] == " ":
    end -= 1
    
manual_stripped_str = str1[start:end+1]
print("The manually stripped string is:", manual_stripped_str)