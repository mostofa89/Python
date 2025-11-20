books_price = {
    "Book A": 29.99,
    "Book B": 39.99

}

new_books = {
    "Book C": 24.99,
    "Book D": 34.99
}

print(f"Books Price Before Update: {books_price}")
books_price.update(new_books)
print(f"Books Price After Update: {books_price}")