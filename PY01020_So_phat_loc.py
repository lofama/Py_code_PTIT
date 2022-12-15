def check(s):
    if s[len(s)-2] =='8' and s[len(s)-1]=='6':
        return True
    return False

t = int(input())
while t>0:
    s = input()
    if check(s):
        print("YES")
    else: print("NO")
    t-=1