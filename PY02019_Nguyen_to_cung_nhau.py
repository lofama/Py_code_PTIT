from math import gcd
t = int(input())
a = [int(x) for x in input().split()]
a = sorted(a,reverse=False)
for i in range(t-1):
    for j in range(i+1,t):
        if gcd(int(a[i]),int(a[j])) == 1:
            print(a[i],a[j])
