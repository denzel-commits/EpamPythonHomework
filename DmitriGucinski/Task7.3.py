from time import perf_counter

def timeit(func):  
    def wrapper():        
        s = perf_counter()
        result = func()        
        e = perf_counter() - s
        print(f'{func.__name__} time {e}')        
        return result
    return wrapper
        
        
@timeit
def workload():
    d = 0
    for i in range(10000):
        d += d ** 2
        
        
workload()
