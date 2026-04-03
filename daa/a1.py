import time

# Iterative function
def iterative(n):
    total = 0
    while n != 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total


# Recursive function
def recursive(n, sum1, temp):
    if n == 0:
        return sum1
    else:
        temp = n % 10
        sum1 += temp
        n = n // 10
        return recursive(n, sum1, temp)


# Input
id = int(input("Enter an id: "))
print(f"ID: {id}")


# Iterative timing
start = time.perf_counter()
ans = iterative(id)
end = time.perf_counter()

print(f"Iterative ans: {ans}")
print(f"Execution Time: {end - start:.8f}")


# Recursive timing
start = time.perf_counter()
ans2 = recursive(id, 0, 0)
end = time.perf_counter()

print(f"Recursive ans: {ans2}")
print(f"Execution Time: {end - start:.8f}")