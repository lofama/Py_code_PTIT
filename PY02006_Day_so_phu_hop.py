t = int(input())
while(t>0):
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(z) for z in input().split()]
    a.sort()
    b.sort()
    flat = 0
    for i in range (n):
        if a[i]>b[i]:
            flat = 1
            print("NO")
            break
    if flat == 0:
        print("YES")