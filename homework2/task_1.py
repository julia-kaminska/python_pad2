def tetranacci_cache(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@tetranacci_cache
def tetranacci(steps):
    if steps < 4:
        return [0, 0, 0, 1][steps]
    else:
        values = [0, 0, 0, 1]
        for _ in range(steps - 3):
            next_value = sum(values)
            values = values[1:] + [next_value]
        return values[-1]
