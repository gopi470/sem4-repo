def merge(A, low, mid, high):
    i, j = low, mid + 1
    temp = []
    inv = 0

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            inv += (mid - i + 1)
            j += 1

    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= high:
        temp.append(A[j])
        j += 1

    A[low:high+1] = temp
    return inv


def mergesort(A, low, high):
    inv = 0
    if low < high:
        mid = (low + high) // 2
        inv += mergesort(A, low, mid)
        inv += mergesort(A, mid + 1, high)
        inv += merge(A, low, mid, high)
    return inv


arr = [7, 5, 3, 1]
print("Number of Inversions =", mergesort(arr, 0, len(arr)-1))
