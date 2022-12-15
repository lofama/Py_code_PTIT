from math import gcd

t = int(input())
while(t>0):
    t-=1
    s = input()
    num1 = int(s)
    x = ""
    for i in s: x=i+x
    num2 = int(x)
    if gcd(num1,num2) == 1: print("YES")
    else: print("NO")