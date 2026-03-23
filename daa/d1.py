def find_max(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    max1 = find_max(arr, left, mid)
    max2 = find_max(arr, mid + 1, right)

    return max(max1, max2)


arr = [15, 42, 7, 29, 88, 54]
result = find_max(arr, 0, len(arr) - 1)

print("Maximum element =", result)
