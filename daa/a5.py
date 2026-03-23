import time


def iterative(arr, lenn):
    for i in range(1, lenn):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def recursive(arr, n):
    if n <= 1:
        return

    recursive(arr, n - 1)

    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key




arr = []

lenn = int(input("Enter the size : "))

print("Enter the array :")
for i in range(lenn):
    temp = int(input())
    arr.append(temp)


arr_iter = arr.copy()
arr_rec = arr.copy()


start = time.perf_counter()
iterative(arr_iter, lenn)
end = time.perf_counter()
print("Iterative Sorted Array :", arr_iter)
print(f"Execution Time : {end - start:.8f}")


start = time.perf_counter()
recursive(arr_rec, lenn)
end = time.perf_counter()
print("Recursive Sorted Array :", arr_rec)
print(f"Execution Time : {end - start:.8f}")
