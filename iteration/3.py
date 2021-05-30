import math


def func(x):
    return math.exp(x) + 10 * x - 2


def func2(x):
    return math.exp(x) + 10


a, k = 0, 0
y = func(a)
print('{:<30}{:<30}{:<30}'.format('k', 'x(k)', 'y(x)'))
print('{:<30}{:<30}{:<30}'.format(k, a, y))
while abs(y) > 0.0005:
    a = a - func(a) / func2(a)
    y = func(a)
    k += 1
    print('{:<30}{:<30}{:<30}'.format(k, a, y))
