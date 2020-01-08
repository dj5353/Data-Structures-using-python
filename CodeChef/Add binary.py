def add_Binary(a,b):
    x = int(a,2)
    y = int(b,2)
    z = bin(x + y)
    return str(z[2::])

print(add_Binary(a="100",b="101"))
