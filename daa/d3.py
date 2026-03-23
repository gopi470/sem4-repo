def partition(A, low, high):
    pivot = A[high]
    i = low

    for j in range(low, high):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[high] = A[high], A[i]
    return i


def quickselect(A, low, high, k):
    if low <= high:
        pi = partition(A, low, high)

        if pi == k:
            return A[pi]
        elif pi < k:
            return quickselect(A, pi + 1, high, k)
        else:
            return quickselect(A, low, pi - 1, k)


arr = [7, 5, 3, 1, 12, -16, 4, -2]
k = 3
n = len(arr)

target = n - k
result = quickselect(arr, 0, n - 1, target)

print("kth largest element =", result)
