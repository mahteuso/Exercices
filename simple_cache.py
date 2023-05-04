from collections import deque

cache_values = deque()

def cache(func):
    def inner(*args):
        cache_values.append(args)
        return func(*args)
    return inner

@cache
def sum(*args: int) -> int:
    result = 0
    for arg in args:
        result += arg
    return result
