import math
def nto(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0 : return False
    return True
m = {}
n = int(input())
a = [int(x) for x in input().split()]
for i in range(len(a)):
    if(a[i]!=0 and nto(a[i])):
        dem = 1
        for j in range(i+1,len(a)):
            if a[j] == a[i] and a[j]!=0:
                dem+=1
                a[j]=0
        print(a[i]," ",dem)
    