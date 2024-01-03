from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"Elapsed time: {t2 - t1} seconds")
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()