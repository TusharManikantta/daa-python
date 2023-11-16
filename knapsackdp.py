def knapSack(W,wt,val,n):
    dp=[0 for i in range(W+1)]
    for i in range(1,n+1):
        for w in range(W,0,-1):
            if wt[i-1] <=w:
                dp[w]= max(dp[w],dp[w]-wt[i-1]+val[i-1])
    return dp[W]


if __name__=='__main__':
    n=int(input("enter the number of items: "))
    profit=[int(x) for x in input("enter the profit seperated by space: ").split()]
    weight=[int(x) for x in input("enter the weights seperated by space: ").split()]
    W=int(input("Enter the knapsack capacity"))

    print(knapSack(W,weight,profit,n))
