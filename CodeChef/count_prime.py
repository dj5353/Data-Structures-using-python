def fast_prime(n):
    if(n<3):return 0
    lst = [1] * n
    lst[0] = lst[1] = 0
    m = 2
    while(m*m < n):
        lst[m*m:n:m] = [0] * (1+(n-m * m-1)//m)
        if(m == 2):
            m+=1
        else:m += 2
    return sum(lst)
print(fast_prime(2100))

def countPrime(n):
    prime = [None]*(n+1)
    prime[0] = prime[1] = 0
    if n<2:
        return
    else:
        for i in range(2,n+1):
            if prime[i] != 0:
                prime[i] = 1
            for j in range(i*i,n+1,i):
                prime[j] = 0
    return sum(prime)
print(countPrime(21))



