a,b=map(int,input().split())

i = min(a, b)
while not (a%i==0 and b%i==0):
    i -= 1
print(i)

i=max(a,b)
while i%a!=0 or i%b!=0:
    i+=max(a,b)
print(i)