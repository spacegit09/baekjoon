import sys
input = sys.stdin.readline

n=int(input())
c=map(int,input().split())
d=dict()
m=int(input())
a=map(int,input().split())
for e in c:
    if d.get(e)==None:
        d[e]=1
    else:
        d[e]+=1
for e in a:
    if d.get(e)!=None:
        print(d.get(e),end=" ")
    else:
        print(0,end=" ")
        