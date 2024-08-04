t=int(input())
for _ in range(t):
    c=int(input())
    q=c//25
    c-=q*25
    d=c//10
    c-=d*10
    n=c//5
    c-=n*5
    print(q,d,n,c)
