def check(s):
    for i in range(len(s)):
        if s[i] != '1' and s[i] != '2' and s[i]!='0' :
            return False
    return True

t = int(input())
while t>0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t-=1