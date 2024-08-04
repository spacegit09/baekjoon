n=int(input())
count=1
room=1
while count<n:
    count+=6*room
    room+=1
print(room)