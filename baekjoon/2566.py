arr=[]
max=-1
max_x=0
max_y=0
for _ in range(9):
    arr.append(list(map(int,input().split())))
for y in range(9):
    for x in range(9):
        if arr[y][x]>max:
            max=arr[y][x]
            max_x=x
            max_y=y
print(max)
print(max_y+1,max_x+1)