def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
N = int(input("Enter the number"))
for i in range(N):
    gold = [0,1,2,3,5,8,13,21,34,55,89,123,136,141,143]
    if i%144 not in gold:
        continue
    else:
        print(fibo(i))
        
