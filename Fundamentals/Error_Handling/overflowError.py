def power(base: int, exponent: int) -> int:
    try:
        result = base ** exponent
        
        if result > 1e18:  # Arbitrary large number to simulate overflow
            raise OverflowError("The result is too large and causes an overflow.")
        
        return result
    
    except OverflowError as oe:
        return str(oe)
    

# Example usage
print(power(2, 10))   # Output: 1024
print(power(10, 20))  # Output: The result is too large and causes an overflow.