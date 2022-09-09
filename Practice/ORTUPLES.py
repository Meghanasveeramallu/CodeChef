# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    p=[1,0,1,4]
    q=1 
    for i in range(30):
        q=q*p[((a>>i)&1)+((b>>i)&1)+((c>>i)&1)]
    print(q)
