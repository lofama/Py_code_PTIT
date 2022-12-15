def check(x):
    s = str(x)
    if len(s)%2>0: return False
    for i in range(len(s)):
        if int(s[i])%2!=0: return False
        if s[i]!=s[len(s)-1-i]: return False
    return True
t = int(input())
while t>0:
    t-=1
    a = int(input())
    for i in range(22,a,2):
        if check(i):
            print(i, end=" ")
    print()