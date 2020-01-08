#a**2  +  b**2 = c
#b = (c - a**2)**2
def sumOfsquareNum(n):
    for a in range(0,int((n**0.5)+1)):
        b = (n - a**0.5)**0.5
        if b == int(b):
            return True
    else:
        return False
print(sumOfsquareNum(10))
