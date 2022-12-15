def check(s):
    sum = 0
    for i in range(len(s)):
        sum+=int(s[i])
    s = str(sum)
    if len(s) < 2 : return False
    for i in range(int(len(s)/2)+1):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

t = int(input())
while t>0:
    s = input()
    if(check(s)): print("YES")
    else: print("NO")
    t-=1