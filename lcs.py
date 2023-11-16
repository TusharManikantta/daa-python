def lcs(X,Y,m,n):
    if m==0 or n==0:
        return 0
    elif X[m-1]==Y[n-1]:
        return 1+lcs(X,Y,m-1,n-1)
    else:
        return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1))
    

if __name__ == '__main__':
    s1=input("enter the first string:")
    s2=input("Enter the second string: ")
    result=lcs(s1,s2,len(s1),len(s2))
    print("len of lcs is: ",result)

