def is_exist(x):
    l=0
    r=n-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            return 1
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
    return 0

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()

for t in b:
    print(is_exist(t))

