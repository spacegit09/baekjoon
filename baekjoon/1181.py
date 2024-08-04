import sys
input = sys.stdin.readline
n=int(input())
s=set()
for _ in range(n):
    s.add(input().strip())
s=list(s)
s.sort(key=lambda x:(len(x),x))
for e in s:
    print(e)
