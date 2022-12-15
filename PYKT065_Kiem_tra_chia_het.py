import math


def nto(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def day(n):
    h=0
    for i in range(2, n+1):
        if nto(i):
            h+=1
    a = [0]*h
    h = 0
    for i in range(2, n+1):
        if nto(i):
            a[h]= i
            h+=1
    return a


while True:
    s = input()
    if s == "-1":
        break
    l, r = [int(x) for x in s.split()]
    n = int(input())
    so = 0
    a = day(n)
    for i in range(l, r+1):
        dem = 0
        for j in range(len(a)):
            if i % int(a[j]) == 0:
                dem = 1
                break
        if dem == 0:
            so += 1
    print(so)
