def divide_numbers(a, b):
    try:
        result = a / b
        return result
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
# Example usage
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error: Cannot divide by zero.