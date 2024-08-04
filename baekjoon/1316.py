def checker(s):
    set_ = set()
    for i in range(len(s)):
        if s[i] not in set_ or i>0 and s[i]==s[i-1]:
            set_.add(s[i])
            continue
        return False
    return True
cnt=0
for _ in range(int(input())):
    if checker(input()):
        cnt+=1
print(cnt)

