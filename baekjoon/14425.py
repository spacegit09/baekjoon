import sys
input = sys.stdin.readline

n,m=map(int,input().split())
s=set()
cnt=0
for _ in range(n):
    s.add(input())
for _ in range(m):
    if input() in s:
        cnt+=1
print(cnt)