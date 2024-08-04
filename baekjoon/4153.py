while True:
    sum=0
    a=list(map(int,input().split()))
    if a[0]==0:
        break
    maximum=max(a)
    for e in a:
        if e!=maximum:
            sum+=e**2
    if sum==maximum**2:
        print("right")
    else:
        print("wrong")