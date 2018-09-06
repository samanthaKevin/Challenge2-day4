def recursive_power(a,b):
    if b == 1:
        return a
    else:
        return (a * recursive_power(a,b-1))
