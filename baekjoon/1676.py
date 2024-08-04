def count5(x):
    count=0
    while x%5==0:
        x//=5
        count+=1
    return count

n=int(input())
c=0
for i in range(1,n+1):
    c += count5(i)
print(c)