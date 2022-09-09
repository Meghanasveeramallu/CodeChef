# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    m=int(input())
    b=[int(s) for s in input().split()]
    s=set()
    for x in b:
        s.add(x)
    for i in range(n):
        if a[i] not in s:
            print(a[i],end=' ')
    print()
