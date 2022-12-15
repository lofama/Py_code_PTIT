def check(s):
    x = ""
    for i in s : x = i+x
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(x[i])-ord(x[i-1])): return False
    return True

t = int(input())
while t>0:
    t-=1
    s = input()
    if check(s): print("YES")
    else : print("NO")