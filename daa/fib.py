def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)

def iter_fib(n):
    a,b = 0,1
    for _ in range(n): 
        a, b = b, a+b
    return a

print(recursive_fib(20))  # Output: 55
print(iter_fib(20))  # Output: 55
