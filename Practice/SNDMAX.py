t=int(input())
for i in range(t):
    a=[int(s) for s in input().split()]
    maxi=a[0]
    smax=0
    for i in range(1,len(a)):
        if a[i]>maxi:
            smax=maxi
            maxi=a[i]
        elif a[i]<maxi and a[i]>smax:
            smax=a[i]
    print(smax)
