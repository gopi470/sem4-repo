#Computing Power using Divide and Conquer (Fast Exponentiation)

def power(x, n):
    if n == 0:
        return 1

    half = power(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


x = 2
n = 10
print("Result =", power(x, n))




# power(2,10)
# → power(2,5)
# → power(2,2)
# → power(2,1)
# → power(2,0) = 1


# power(2,1) = 2
# power(2,2) = 4
# power(2,5) = 32
# power(2,10) = 1024


#T(n) = T(n/2) + O(1)

#T(n) = O(log n)
