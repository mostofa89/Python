book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)
for i in range(len(book_info)):
    a, b, c = book_info[i]
    print(str(b),"won the", str(a), str(c),"votes")