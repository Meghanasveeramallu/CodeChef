t=int(input())
for i in range(t):
    x,y,n=map(int,input().split())
    if (n>=x and n<y):
        print("YES")
    else:
        print("NO")
