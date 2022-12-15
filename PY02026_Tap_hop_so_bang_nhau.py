sm={}
sn={}
n,m = [int(x) for x in input().split()]
s1 = input().split()
s2 = input().split()
for i in s1:
    sm[i] =1
for i in s2:
    sn[i]=1
if sm == sn:
    print("YES")
else:
    print("NO")