str1 = "Hello World"

appearance_count = str1.count('o')
print("The character 'o' appears", appearance_count, "times in the string.")

# Manual counting of character 'o'
counter = 0
for char in str1:
    if char == 'o':
        counter += 1

print("The character 'o' appears", counter, "times in the string (calculated manually).")