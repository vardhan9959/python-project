def calculate_average(numbers):
  if not numbers:
    return None
  total = sum(numbers)
  average = total / len(numbers)
  return average
number_list = [23, 56, 78, 12, 45]
average_result = calculate_average(number_list)
if average_result is not None:
  print(f"The average is: {average_result}")
else:
  print("The list is empty.")

  