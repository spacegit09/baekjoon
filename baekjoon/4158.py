while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    a=[]
    b=[]
    cnt=0
    for _ in range(n):
        a.append((int(input())))
    for _ in range(m):
        b.append(int(input()))

    for t in b:
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if t==a[mid]:
                cnt+=1
                break
            elif a[mid]>t:
                r=mid-1
            else:
                l=mid+1
    print(cnt)
