def unique_paths(m, n):
    dp = [[0]*n for _ in range(m)]

    # First column
    for i in range(m):
        dp[i][0] = 1

    # First row
    for j in range(n):
        dp[0][j] = 1

    # Fill
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


print("Number of Unique Paths =", unique_paths(3, 3))