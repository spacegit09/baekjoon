arr=[]
result=""
for _ in range(5):
    arr.append(input())
for x in range(15):
    for y in range(5):
        if len(arr[y])>x:
            result+=arr[y][x]
print(result)

