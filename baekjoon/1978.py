def is_prime(x):
    if x==1:
        return False
    for divisor in range(2,x):
        if x%divisor == 0:
            return False
    return True 

n=int(input())
arr=map(int,input().split())
cnt=0
for dividend in arr:
    if is_prime(dividend):
        cnt+=1
print(cnt)
        
