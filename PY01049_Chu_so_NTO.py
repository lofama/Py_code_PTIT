def nto(x):
    x = int(x)
    if x < 2 : return False
    else:
        for i in range(2, x):
            if x % i ==0:
                return False
    return True
def check(s):
    if s =='2' or s=='3' or s == '5' or s=='7':
        return True
    return False

t = int(input())
while t>0:
    s = input()
    dem = 0
    for i in range(len(s)):
        if check (s[i]): dem+=1
    if dem*2>len(s) and nto(len(s)):
        print("YES")
    else :
        print("NO")
    t-=1