# def candy(ratings):
#     n = len(ratings)
#     if n == 0:
#         return 0
#     candies = [1] * n
# # Left to right pass
#     for i in range(1, n):
#         if ratings[i] > ratings[i - 1]:
#             candies[i] = candies[i - 1] + 1
#     # Right to left pass
#     for i in range(n - 2, -1, -1):
#         if ratings[i] > ratings[i + 1]:
#             candies[i] = max(candies[i], candies[i + 1] + 1)
#     return sum(candies)
# # Example usage:
# if __name__ == "__main__":
#     ratings = [1, 0, 2]
#     print("Minimum candies required:", candy(ratings))  # Output: 5



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
elements = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(elements)
bubble_sort(elements)
print("Sorted list is:")
print(elements)
