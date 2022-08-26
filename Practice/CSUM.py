t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(s) for s in input().split()]
    a.sort()
    p=0
    q=n-1
    while(p<q):
        if (a[p]+a[q]==k):
            print("Yes")
            break
        elif (a[p]+a[q]>k):
            q-=1 
        else:
            p+=1 
    if (p>=q):
        print("No")
