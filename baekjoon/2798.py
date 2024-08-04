n,m=map(int,input().split())
cards=list(map(int,input().split()))
result=0
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            s=cards[a]+cards[b]+cards[c]
            if s<=m and s>result:
                result=s
print(result)
            