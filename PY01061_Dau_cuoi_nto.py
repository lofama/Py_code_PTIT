import math
def nto(x):
    if x < 2: return False
    for i in range (2,int(math.sqrt(x)+1)):
        if x % i == 0: return False
    return True
t = int(input())
while t>0:
    t-=1
    s = input()
    sum1 =int(s[0])*100+int(s[1])*10+int(s[2])
    sum =int(s[-3])*100+int(s[-2])*10+int(s[-1])
    if(nto(sum) and nto(sum1)):
        print("YES")
    else: 
        print("NO")