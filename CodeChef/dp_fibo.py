def fibo(n):
    dp = [None] * (n+1)
    if n == 0 or n == 1:
        dp[n] = n
    
    if dp[n] is None:
        dp[n] =  fibo(n-1) + fibo(n-2)    
    return (dp[n])
print(fibo(8))
0,1,1,2,3,5,8,13,21 