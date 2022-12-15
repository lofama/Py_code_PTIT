from math import gcd
x,n = input().split()
x = int(x)
n = int(n)
dem = 0
for i in range(10**(n-1),10**n,1):
    if gcd(x,i)==1:
        print(i,end = " ")
        dem+=1
        if dem == 10:
            print()
            dem = 0