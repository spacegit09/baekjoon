def check(x):
    if x == 666:
        return True
    for i in range(len(str(x)) - 2):
        temp=x
        temp//=(10**i)
        temp%=1000
        if temp==666:
            return True
    return False

n=int(input())
i=0
count=0
while True:
    i+=1
    if check(i):
        count+=1
    if count==n:
        break
print(i)

