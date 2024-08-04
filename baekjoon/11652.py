import sys
input=sys.stdin.readline
n=int(input())
d=dict()
for _ in range(n):
    c=int(input())
    if d.get(c)==None:
        d[c]=1
    else:
        d[c]+=1

m_key = list(d.keys())[0]

for k, v in d.items():
    if v > d[m_key]:
        m_key=k
    elif v == d[m_key]:
        m_key = min(k, m_key)

print(m_key)

