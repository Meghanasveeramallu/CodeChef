t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    l1 = list(range(1, l[0]+1))
    l1[0], l1[l[0] -1 - l[1]] = l1[l[0] -1 - l[1]], l1[0]
    print(*l1, sep = ' ')
