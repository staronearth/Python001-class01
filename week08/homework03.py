import time
def timer(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        diss_time = time.time()-start_time
        print(diss_time)
    return inner

@timer
def fib(n):
    res = 1
    for i in range(n):
        res =  i * res
    return res

fib(10000000)

