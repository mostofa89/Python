books = {
    "Book A": 29.99,
    "Book B": 39.99

}

print(f"Books Before popitem: {books}")
removed_item = books.popitem()
print(f"Removed Item: {removed_item}")
print(f"Books After popitem: {books}")