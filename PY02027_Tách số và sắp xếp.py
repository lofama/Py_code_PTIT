ans = []
s=""
t = int(input())
for i in range(t):
    s+=input()
    s+='z'
n = len(s)
so=-1
for i in range(n):
    if s[i].isalpha():
        if so > -1:
            ans.append(so)
            so = -1
    else:
        if s[i].isdigit():
            if so == -1: so = 0
            so =so*10+int(s[i])
ans.sort()
for i in ans:
    print(i)