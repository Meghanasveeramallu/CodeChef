# cook your dish here
def f(n,k):
    if n==1 and k==1:
        return "YES"
    if n<=k:
        return "NO"
    if n-k>=(k-1)*(k)/2:
        return "YES"
    return "NO"

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    print(f(n,k))
