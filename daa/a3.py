import time


def iterative(x,n):
    total = 1
    while n != 0:
        total *= x
        n-=1 
    return total


def recursive(x,n):

    if(n==0): 
        return 1
       
    return x * recursive(x,n-1)





x =int(input("Enter base :"))
n =int(input("Enter power :"))

print(f"Base : {x} ")
print(f"Power : {n} ")

print('-----------------------------------------')

start=time.perf_counter()
ans = iterative(x,n)
end=time.perf_counter()
print(f"Iterative ans: {ans}")
print(f"Execution Time : {end -start:.8f}")

print('-----------------------------------------')

start=time.perf_counter()
ans2 = recursive(x,n)
end=time.perf_counter()
print(f"Recersive ans: {ans2}")
print(f"Execution Time : {end -start:.8f}")

