def grad_descent(start, rate, n):
    x = start
    for i in range(n):
        grad = 2 * (x + 3)
        x = x - (rate * grad)
        print(f"iteration {i+1}, x: {x}, y:{(x+3)**2}")
    return x

start = 2
l_rate = 0.09
n = 10

final_x = grad_descent(start,l_rate,n)
print(f"x: {final_x}, y: {(final_x+3)**2}")
