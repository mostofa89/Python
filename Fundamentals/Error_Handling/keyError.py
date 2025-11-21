def find_Element(dct, key):
    try:
        return dct[key]
    except KeyError:
        return "Key not found. Please provide a valid key."
    

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(find_Element(my_dict, 'b'))  # Output: 2
print(find_Element(my_dict, 'x'))  # Output: Key not found. Please provide a valid key.
