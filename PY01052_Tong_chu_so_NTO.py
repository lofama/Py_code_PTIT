def check(s):
    sum = 0
    for i in range(len(s)):
        sum+=int(s[i])
    x = sum
    if x < 2 : return False
    else:
        for i in range(2, x):
            if x % i ==0:
                return False
    return True    

t = int(input())
while t>0:
    s = input()
    if(check(s)): print("YES")
    else: print("NO")
    t-=1