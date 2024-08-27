str1 : str = "AJAJG qwert"
upper_str = ""
lower_str = ""

for ch in str1:
    if ord(ch) >= 97 and ord(ch) <= 122:
        lower_str += ch
        upper_str += chr(ord(ch) - 32)

    elif ord(ch) >= 65 and ord(ch) <= 90:
        upper_str += ch
        lower_str += chr(ord(ch) + 32)

    else:
        upper_str += ch
        lower_str += ch

print(f"Upper case : {upper_str}.\nLower  case : {lower_str}.")