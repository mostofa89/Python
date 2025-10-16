flag = True
is_valid = False

flot_flag = float(flag)
flot_is_valid = float(is_valid)

print(f"Type of flag: {type(flag)}")                # Output: <class 'bool'>
print(f"Type of is_valid: {type(is_valid)}")        # Output: <class 'bool'>
print(f"Type of flot_flag: {type(flot_flag)}")      # Output: <class 'float'>
print(f"Type of flot_is_valid: {type(flot_is_valid)}")  # Output: <class 'float'>
print(f"Value of flag: {flag}")                      # Output: True
print(f"Value of is_valid: {is_valid}")              # Output: False
print(f"Value of flot_flag: {flot_flag}")            # Output: 1.0
print(f"Value of flot_is_valid: {flot_is_valid}")    # Output: 0.0
print(f"Sum of flot_flag and flot_is_valid: {flot_flag + flot_is_valid}")  # Output: 1.0