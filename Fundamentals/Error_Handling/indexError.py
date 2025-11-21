def find_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range. Please provide a valid index."
    

# Example usage
my_list = [10, 20, 30, 40, 50]
print(find_element(my_list, 2))   # Output: 30
print(find_element(my_list, 10))  # Output: Index out of range. Please provide a valid index.