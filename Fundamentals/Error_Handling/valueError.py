def check_positive_number(value : int) -> None:
    try:
        if type(value) != int:
            raise ValueError("The number must be Integer.")
        
        if value <= 0:
            raise ValueError("The number must be positive.")
        
        if value > 0:
            return "The number is positive."
        
    except ValueError as ve:
        return str(ve)
    


# Example usageprint(check_positive_number(10))   # Output: The number is positive.
print(check_positive_number(-5))  # Output: The number must be positive.
print(check_positive_number("abc"))  # Output: ValueError: The number must be positive.
print(check_positive_number(0))   # Output: The number must be positive.# Example usage
print(check_positive_number(10))   # Output: The number is positive.