# cook your dish here
t=int(input())
for i in range(t):
    mean,median=map(int,input().split())
    if mean==median:
        print(mean,mean,mean)
    else:
        print(-501,median,mean*3 +501-median)
