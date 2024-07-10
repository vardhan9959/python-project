def sort_numbers(numbers, ascending=True):
    sorted_numbers = sorted(numbers, reverse=not ascending)
    return sorted_numbers
numbers_to_sort = [5, 2, 8, 1, 7]
ascending_result = sort_numbers(numbers_to_sort, ascending=True)
print("Ascending Order:", ascending_result)
descending_result = sort_numbers(numbers_to_sort, ascending=False)
print("Descending Order:", descending_result)
