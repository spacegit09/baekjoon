n,m=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))
for y in range(n):
    for x in range(m):
        print(a[y][x]+b[y][x],end=' ')
    print()