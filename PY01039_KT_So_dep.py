def check(s):
    for i in range(len(s)-2): 
        if s[i] !=s [i+2]: return False
    if s[0]==s[1]: return False
    return True

t =int(input())
while t>0:
    s =input()
    if check(s): print("YES")
    else: print("NO")
    t-=1