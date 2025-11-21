def divide_numbers(a, b):
    try:
        result = a / b
        return result
    
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    

# Example usage
print(divide_numbers(10, 2))        # Output: 5.0
print(divide_numbers(10, 'a'))      # Output: Error: Invalid input type.    
print(divide_numbers('x', 'y'))    # Output: Error: Invalid input type.