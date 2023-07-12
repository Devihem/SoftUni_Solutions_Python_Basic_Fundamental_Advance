def cache(func):
    def wrapper(*args):
        cache_key = args[0]
        if cache_key not in wrapper.log:
            wrapper.log[cache_key] = func(*args)
        return wrapper.log[cache_key]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(7)
print(fibonacci.log)