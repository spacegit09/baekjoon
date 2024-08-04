arr=[]
for _ in range(9):
    arr.append(int(input()))
arr.sort()
total=sum(arr)
for i in range(0,8):
    for j in range(i+1,9):
        if total-arr[i]-arr[j]==100:
            arr.pop(j)
            arr.pop(i)
            for e in arr:
                print(e)
            exit(0)
