# def lcs(X,Y,m,n):
#     if m==0 or n==0:
#         return 0
#     elif X[m-1]==Y[n-1]:
#         return 1+lcs(X,Y,m-1,n-1)
#     else:
#         return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1))
    


# s1=input("enter the first string:")
# s2=input("Enter the second string: ")
# result=lcs(s1,s2,len(s1),len(s2))
# print("len of lcs is: ",result)



def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0, []

    if X[m - 1] == Y[n - 1]:
        length, sequence = lcs(X, Y, m - 1, n - 1)
        return length + 1, sequence + [X[m - 1]]
    else:
        length1, sequence1 = lcs(X, Y, m - 1, n)
        length2, sequence2 = lcs(X, Y, m, n - 1)
        if length1 > length2:
            return length1, sequence1
        else:
            return length2, sequence2


s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
length, longest_subsequence = lcs(s1, s2, len(s1), len(s2))

print("Length of LCS is:", length)
print("Longest Subsequence:", "".join(longest_subsequence))
