import math

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Create temporary arrays
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + 1 + j]

    # Add sentinel values (infinity) at the end of the arrays
    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    # Merge the temp arrays back into A[p..r]
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Example usage
A = [38, 27, 43, 3, 9, 82, 10]
merge_sort(A, 0, len(A) - 1)
print("Sorted array:", A)
