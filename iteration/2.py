import math


def func(x):
    return math.exp(x) + 10 * x - 2


a, k = 0, 0
y = func(a)
print('{:<30}{:<30}{:<30}'.format(' ', 'x(k+1)', 'y(x)'))
print('{:<30}{:<30}{:<30}'.format('x(' + str(k) + ')', a, y))
while abs(y) > 0.0005:
    a = (2 - math.exp(a)) / 10
    y = func(a)
    k += 1
    print('{:<30}{:<30}{:<30}'.format('x(' + str(k) + ')', a, y))
