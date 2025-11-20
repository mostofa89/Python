original_dict = {'a': 1, 'b': 2}
print(f"Original Dictionary: {original_dict}")

copied_dict = original_dict.copy()
print(f"Copied Dictionary: {copied_dict}")

copied_dict['c'] = 3
print(f"Modified Copied Dictionary: {copied_dict}")
