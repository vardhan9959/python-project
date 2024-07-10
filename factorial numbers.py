def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
calculate_factorial = 5
result = factorial(calculate_factorial)
print(f"The factorial of {calculate_factorial} is: {result}")