def lis(arr):
    n = len(arr)
    dp = [1] * n

    # Step 3: Fill dp
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Step 4: length
    length = max(dp)

    # Step 5–8: reconstruct LIS
    lis_seq = []
    curr = length

    for i in range(n-1, -1, -1):
        if dp[i] == curr:
            lis_seq.append(arr[i])
            curr -= 1

    lis_seq.reverse()

    return length, lis_seq


arr = [10, 9, 2, 5, 3, 7, 101, 18]
length, seq = lis(arr)
print("Length of LIS =", length)
print("LIS =", seq)