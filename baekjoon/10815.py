import sys
input=sys.stdin.readline
n=int(input())
c=set(map(int,input().split()))
m=int(input())
a=map(int,input().split())
for e in a:
    if e in c:
        print("1", end=" ")
    else:
        print("0", end=" ")
