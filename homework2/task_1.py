def cache_decorator(func):
    cache = {}

    def wrapper(self, n):
        if n not in cache:
            cache[n] = func(self, n)
        return cache[n]

    return wrapper

class Tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.counter = 0
        self.values = [0, 0, 0, 1]

    @cache_decorator
    def calculate_tetranacci(self, n):
        if n <= 3:
            return self.values[n]
        else:
            next_value = sum(self.values)
            self.values = self.values[1:] + [next_value]
            return next_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.steps:
            self.counter += 1
            result = self.calculate_tetranacci(self.counter - 1)
            return result
        else:
            raise StopIteration

