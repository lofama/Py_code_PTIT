import math
def nto(x):
    if x < 2: return False
    for i in range (2,int(math.sqrt(x))+1):
        if x%i==0: return False
    return True

t = int(input())
a = {2,3,5,7}
while(t>0):
    n =input()
    for i in range(len(n)):
        if(nto(i)):
            if(int(n[i]) in a):
                i+=0
            else :
                print("NO")
                break
        else :
            if(int(n[i]) in a):
                print("NO")
                break
        if i ==len(n)-1: print("YES")
    t-=1