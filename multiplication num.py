def multiplication_table(number, table_size):
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, table_size + 1):
        result = number * i
        print(f"{number} x {i} = {result}")
given_number = 7
table_size = 10

multiplication_table(given_number, table_size)
