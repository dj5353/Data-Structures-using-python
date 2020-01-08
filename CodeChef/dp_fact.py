#dynamic programming have linear time complexity while recurrsion have exponential time complexity.
def fact(n):
    dp = [None]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1] * i
    return (dp[i])
print(fact(1024))

