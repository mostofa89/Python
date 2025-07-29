dict1={'Harry':15, 'Draco':8, 'Nevil':19}
# dict2={'Ginie':18, 'Luna': 14}

for key in dict1:
    # print(key) # print the key
    # print(dict1[key]) # print the value of the key
    print(f"{key}: {dict1[key]}")

print("==================================================")

for key, value in dict1.items():
    print(f"{key} : {value}") # printing key value pair