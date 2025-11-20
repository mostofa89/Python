def  sum_of_values(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value

    print(f"The sum of the provided values is: {total}")



sum_of_values(a=10, b=20, c=30)
sum_of_values(x=5, y=15, z=25, w=35)