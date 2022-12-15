import math
def nto(x):
    if x<2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:return False
    return True

t = int(input())
while t>0:
    t-=1
    n = input()
    so=0
    if(nto(len(n))):
        for i in range(len(n)):
            if nto(int(n[i])): so+=1
        if so > len(n)/2:
            print("YES")
        else: print("NO")
    else:
        print("NO")
