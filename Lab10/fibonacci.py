import time
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

start_time = time.time()
print(recur_fibo(35)) 
end_time = time.time()
print(f"Memoized Fibonacci Execution Time: {end_time - start_time} seconds")

def recur_fibo_no_memo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo_no_memo(n-1) + recur_fibo_no_memo(n-2)

start_time = time.time()
print(recur_fibo_no_memo(35))
end_time = time.time()
print(f"Non-Memoized Fibonacci Execution Time: {end_time - start_time} seconds")
