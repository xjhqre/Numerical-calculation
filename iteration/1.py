import math


def func(x):
    return math.exp(x) + 10 * x - 2


a, b = 0, 1
x = (a + b) / 2
y = func(x)
k = 0
print('{:<20}{:<20}{:<20}{:<20}{:<20}'.format('k', 'a', 'b', 'x', 'y(x)'))
print('{:<20}{:<20}{:<20}{:<20}{:<20}'.format(str(k), str(a), str(b), str(x), str(y)))
while abs(y) > 0.0005:
    if y > 0:
        b = x
    elif y < 0:
        a = x
    x = (a + b) / 2
    y = func(x)
    k += 1
    print('{:<20}{:<20}{:<20}{:<20}{:<20}'.format(str(k), str(a), str(b), str(x), str(y)))
