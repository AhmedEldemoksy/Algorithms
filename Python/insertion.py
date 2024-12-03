def insertion_sort(A):
    n = len(A)
    for j in range(1, n):  # start from the second element (index 1)
        key = A[j]  # next key to be inserted
        i = j - 1  # compare with the elements before it
        while i >= 0 and A[i] > key:  # find the correct position for the key
            A[i + 1] = A[i]  # shift elements to the right
            i -= 1  # move left in the sorted part
        A[i + 1] = key  # insert the key in the correct position
    return A

        # Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
