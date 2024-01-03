def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a,b = b,a+b
def list_fib(num):
    a = 0
    b = 1
    L = []
    for i in range(num):
        L.append(a)
        a,b = b,a+b
    return L

for i in fib(1000):
    print(i)