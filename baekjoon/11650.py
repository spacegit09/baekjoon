import sys
input = sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
a.sort()
for x, y in a:
    print(x, y)
