def fibo(n,dp):
    if(n==0 or n==1):
        return n
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fibo(n,dp))
