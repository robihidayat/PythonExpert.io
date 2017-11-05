# decorator
# simplest, lazy
from time import time
# from inspect import getsource, getabsfile


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elepsed', after-before)
        return rv
    return f


def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            before = time()
            for _ in range(n):
                # print('running{.__name__}'.format(f))
                rv = f(*args, **kwargs)
            after = time()
            print('elepsed', after - before)
            return rv
        return wrapper
    return inner


@timer
def add(x, y=10):
    return x+y


@ntimes(1)
def subb(x):
    return x

# print(add(1, 2))
print(subb(100))

# print(getsource(add))
# print(getabsfile(add))

#add.__defaults__
#add.__code__
#add.__code__.co_code
#add.__code__.co_name
#add.__code__.co_varnames





