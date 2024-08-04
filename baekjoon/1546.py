n=int(input())
scores=list(map(int,input().split()))
m = max(scores)
sum=0
for score in scores:
    sum += score/m*100
print(sum/n)