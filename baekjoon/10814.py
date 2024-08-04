import sys
input = sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    a, b = input().split()
    arr.append([int(a),b])
arr.sort(key=lambda x:x[0])
for x,y in arr:
    print(x,y)
    


