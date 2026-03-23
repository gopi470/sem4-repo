

import time


def iterative(arr,lenn,n):
    
	left=0
	right=lenn-1
	while (left<=right):
		mid=(left+right)//2
		if (arr[mid]==n):
			return mid
		elif (arr[mid]>n):
			left = mid + 1
		else:
			right = mid - 1
	return -1

def recursive(arr, n, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return recursive(arr, n, left, mid - 1)
    else:
        return recursive(arr, n, mid + 1, right)


arr = []

lenn=int(input("Enter the size :"))

print("Enter the array :")

for i in range(lenn):
    temp=int(input())
    arr.append(temp)

n=int(input("Enter element to search :"))

start=time.perf_counter()
ans=iterative(arr,lenn,n)
end=time.perf_counter()
print(f"Iterative Search Index: {ans}")
print(f"Execution Time : {end -start:.8f}")


start=time.perf_counter()
ans=recursive(arr, n, 0, lenn - 1)
end=time.perf_counter()
print(f"Recursive Search Index: {ans}")
print(f"Execution Time : {end -start:.8f}")