#Merge Sort

def merge(A, low, mid, high):
    i, j = low, mid + 1
    temp = []

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1

    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= high:
        temp.append(A[j])
        j += 1

    A[low:high+1] = temp


def mergesort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(A, low, mid)
        mergesort(A, mid + 1, high)
        merge(A, low, mid, high)


arr = [7, 5, 3, 1]
mergesort(arr, 0, len(arr) - 1)
print("Sorted array =", arr)
