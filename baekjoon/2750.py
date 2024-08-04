n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

for _ in range(n-1):
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
for e in a:
    print(e)
    