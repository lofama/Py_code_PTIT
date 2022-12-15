t = int(input())
a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while t> 0:
    t-=1
    str1 =""
    s,n = [int (x) for x in input().split()]
    while s > 0:
        str1 = str(a[s%n]) + str1
        s = int(s/n)
    print(str1)