# Learn about decorators
'''Problem 1 = Timing function Execution..
Write a decorator that measures the time a function takes to execute.
'''

import time
def timer(func):
    def wrapper(*args,  **kwargs):
       start = time.time()
       result = func(*args, **kwargs)
       end = time.time()
       print(f"{func.__name__} ran in {end-start}")
       return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

