import math
a,b,v=map(int,input().split())
if a>=v:
    print(1)
else:
    print(math.ceil((v-a)/(a-b))+1)