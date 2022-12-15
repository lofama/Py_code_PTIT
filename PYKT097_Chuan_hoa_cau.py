ds=[]
while True:
    try:
        s=input().lower()
        if s[-1]!='.' and s[-1]!='?' and s[-1]!='!': s+='.'
        ds.append(s)
    except Exception: break
a=[]
for i in ds:
    k=0
    for j in range(len(i)):
        if i[j]=='?' or i[j]=='!' or i[j]=='.':
            a.append(i[k:j+1])
            k=j+1
for i in a:
    kq=i.split()
    if kq[-1]=='?' or kq[-1]=='!' or kq[-1]=='.':
        kq[-2]+=kq[-1]
        kq.pop()
    kq[0]=kq[0].title()
    print(' '.join(kq))