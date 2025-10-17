str1 = "Hello World"
words = str1.split(" ")
print("The words in the string are:", words)

# Manual split implementation
manual_words = []
current_word = ""
for char in str1:
    if char == " ":
        if current_word:
            manual_words.append(current_word)
            current_word = ""
    else:
        current_word += char
     
        
if current_word:
    manual_words.append(current_word)

print("The words in the string calculated manually are:", manual_words)
