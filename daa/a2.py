import time


def iterative(n):
    total = 1
    while n != 0:
        total *= n
        n -=1;  
    return total


def recursive(n):

    if(n==1): 
        return 1
       
    return n * recursive(n-1)





items =int(input("Enter no of items :"))

print(f"Items : {items}")

print('-----------------------------------------')

start=time.perf_counter()
ans = iterative(items)
end=time.perf_counter()
print(f"Iterative ans: {ans}")
print(f"Execution Time : {end -start:.8f}")

print('-----------------------------------------')

start=time.perf_counter()
ans2 = recursive(items)
end=time.perf_counter()
print(f"Recersive ans: {ans2}")
print(f"Execution Time : {end -start:.8f}")

