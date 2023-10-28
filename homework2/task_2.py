def repeat(value, n=None):
    if n is None:
        while True:
            yield value
    else:
        for _ in range(n):
            yield value
