# Cache Return Values 
'''Problem : Implement a decorator that chaches the return values of a function so that when its called with the same arguments, the cached value is returned instea of re-executing the function'''
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
      if args in cache_value:
         return cache_value[args]
      result = func(*args)
      cache_value[args] = result
      return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))