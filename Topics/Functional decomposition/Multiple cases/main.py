def f1(x):
    result = (x ** 2) + 1
    return float(result)


def f2(x):
    result = 1 / (x ** 2)
    return float(result)


def f3(x):
    result = (x ** 2) - 1
    return float(result)


def f(x):
    if x <= 0:
        return f1(x)
    elif 0 < x < 1:
        return f2(x)
    else:
        return f3(x)
