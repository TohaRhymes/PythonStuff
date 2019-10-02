def f_l(x):
    f = []
    if type(x) == int:
        f.append(x)
    else:
        for y in x:
            f.extend(f_l(y))
    return f