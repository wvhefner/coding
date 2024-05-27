import random

random.seed(2100)

def my_func(x):
    return sum(x) / len(x)

ab = [random.random() for _ in range(11)]

print(my_func(ab))
