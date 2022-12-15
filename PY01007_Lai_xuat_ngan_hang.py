t = int(input())
for z in range(t):
    n,x,m = map(float,input().split())
    for i in range(10000):
        tien = n*((1+x/100)**i)
        if(tien > m):
            print(i)
            break