arr=[[0 for _ in range(15)] for _ in range(15)]
for i in range(1,15):
    arr[0][i]=i
for floor in range(1,15):
    for num in range(1,15):
        arr[floor][num]=arr[floor-1][num]+arr[floor][num-1]

t=int(input())
for _ in range(t):
    k=int(input())
    n=int(input())
    print(arr[k][n])