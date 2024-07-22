 
# *Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

# Problem 1

# write a  decorator that measures the time a function takes to exceute
import time

def timer(func):
    def wrapper(*args,**kwargs):
       start=time.time()
       result= func(*args,**kwargs)
       end=time.time()
       print (f"{func.__name__} ran in {end-start} time")
       return result
    return wrapper
@timer
def example_func(n):
    time.sleep(n)
example_func(2)


