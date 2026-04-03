#Quick Sort

def partition(A, low, high):
    pivot = A[high]
    i = low

    for j in range(low, high):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[high] = A[high], A[i]
    return i


def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)


arr = [7, 5, 3, 1, 12, -16, 4, -2]
quicksort(arr, 0, len(arr) - 1)

print("Sorted array =", arr)
