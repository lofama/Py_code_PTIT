t = int(input())
while t>0:
    i = int(input())
    a = [int(x) for x in input().split()]
    if i == 1 : sum = max(a)
    if i == 2: sum = a[1] +a[0]
    if i >= 3 :
        a.sort()
        sum=a[0]+a[1]+a[2]
    print(sum)