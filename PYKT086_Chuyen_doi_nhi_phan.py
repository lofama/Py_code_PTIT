fa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def chuyen(s,x):
    ans=""
    so = 0
    if x == 2: 
        ans = s
        return ans
    if x == 4: so = 2
    if x == 8: so = 3
    if x == 16: so = 4
    h = len(s) % so
    for i in range(len(s)-1,-1,-so):
        if i >= so-1:
            a = 0
            for j in range(so):
                a+=int(s[i-j])*(2**j)
            ans = str(fa[a])+ans  
    if h > 0:
            a = 0
            for j in range(h):
                a+=int(s[i-j])*(2**j)
            ans = str(fa[a])+ans
    return ans
f = open("DATA.in",'r')
t = int(f.readline())
while t>0:
    t-=1
    he = int(f.readline())
    st = str(f.readline().rstrip('\n'))
    print(chuyen(st,he))
