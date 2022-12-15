s = input()
n = int(len(s)/2)*2
m={}
for i in range(0,n,2):
    st = int(s[i])*10+int(s[i+1])
    if st not in m:
        m[st]=1
for i in m:
    print(i,end=" ")