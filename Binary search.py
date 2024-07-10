def sortedarray(Array, i, j, number):
    if i <= j:
        mid = (i + j) // 2
        if number == Array[mid]:
            return mid
        elif number > Array[mid]:
            return sortedarray(Array, mid + 1, j, number)
        else:
            return sortedarray(Array, i, mid - 1, number)
    else:
        return -1  # If the number is not found

Array = [1, 2, 3, 4, 5, 6]
print("Array:", Array)
vardhan = int(input("Which number index do you want to find : "))

result = sortedarray(Array, 0, len(Array) - 1, vardhan)

if result == -1:
    print("Number not found in list.")
else:
    print("Number found at index:", result)
