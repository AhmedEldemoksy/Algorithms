def selection_sort(A):
    n = len(A)
    for j in range(n - 1):
        smallest = j
        for i in range(j + 1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

A = [64, 25, 12, 22, 11]
selection_sort(A)
print("Sorted array:", A)
