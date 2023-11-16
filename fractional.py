class Item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
def fractionalKnapsack(W,arr):
    arr.sort(key=lambda x:(x.profit/x.weight), reverse = True)
    finalvalue=0.0
    for item in arr:
        if item.weight<=W:
            W-=item.weight
            finalvalue+=item.profit
        else:
            finalvalue+=item.profit*W/item.weight
            break
    return finalvalue
W=int(input("enter the max capacity of knapsack:"))
arr=[]
n=int(input("enter the no of items"))
for i in range(n):
    print("enter the profit item:",i+1)
    x=int(input())
    print("enter the weight of item",i+1)
    y=int(input())
    arr.append(Item(x,y))
    max_val=fractionalKnapsack(W,arr)
print("the max profit is: ",max_val)


