import math
f = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def doi(s,he):
    so = int(math.log(he,2))
    n = len(s)
    ans=""
    x = 0
    if he == 2:
        return s
    if n%so > 0:
        for i in range(n%so):
            x+=2**(n%so-1-i)*int(s[i])
        ans+=f[x]
    for i in range(n%so,n,so):
        x = 0
        for j in range(so):
            x+=2**(so-j-1)*(int(s[i+j]))
        ans+=f[x]
    return ans
t = int(input())
while t>0:
    t-=1
    a = int(input())
    st = input()
    ke = doi(st,a)
    print(ke)
