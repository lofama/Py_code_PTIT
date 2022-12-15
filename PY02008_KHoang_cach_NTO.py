import math


def nto(x):
    if x < 2 : return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
n,x = input().split()
n = int(n)
x = int(x)
a = 0
for i in range(n+1):
    x = x+a
    print(x,end=" ")
    for j in range(a+1, 100000,1):
        if nto(j) == True:
            a = j
            break
        else: j+=1
