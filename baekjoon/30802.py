import math
n=int(input())
sizes=map(int,input().split())
t,p=map(int,input().split())
cnt=0
for size in sizes:
    cnt+=math.ceil(size/t)
print(cnt)
print(n//p, n%p)