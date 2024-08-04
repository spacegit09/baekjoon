n=int(input())
arr=[[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    start_x,start_y=map(int,input().split())
    for x in range(start_x,start_x+10):
        for y in range(start_y,start_y+10):
            arr[y][x] = 1
cnt=0
for y in range(100):
    for x in range(100):
        cnt+=arr[y][x]
print(cnt)