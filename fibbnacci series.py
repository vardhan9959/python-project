def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series

# Set the number of terms you want in the Fibonacci series
num_terms = 10

# Print the Fibonacci series
result = fibonacci(num_terms)
print(result)
