def constructor(x):
    result=x
    for c in str(x):
        result+=int(c)
    return result    

n=int(input())
for i in range(n):
    if constructor(i)==n:
        print(i)
        exit(0)
print(0)