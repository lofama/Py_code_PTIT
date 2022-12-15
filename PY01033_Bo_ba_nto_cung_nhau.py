from math import gcd

def check(a,b,c):
    if gcd(a,b)>1: return False
    if gcd(a,c)>1: return False
    if gcd(c,b)>1: return False
    return True
x,y = (int(a) for a in input().split())
for i in range(x,y-1):
    for j in range(i+1,y):
        for k in range(j+1,y+1):
            if check(i,j,k):
                print("("+str(i)+", "+str(j)+", "+str(k)+")")