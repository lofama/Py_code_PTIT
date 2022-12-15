t = int(input())
while t>0:
    t-=1
    n,m = [int(x) for x in input().split()]
    s=[0]*(n+1)
    s1 = input().split()
    h = 0
    for i in s1:
        s[h] = int(i)
        h+=1
    for i in range(h):
        if s[i] == max(s):
            for j in range(h,i,-1):
                s[j]=s[j-1]
            s[i]=m
            break
    k=0
    for i in range(h+1):
        if s[i] < 0:
            tmp = s[i]
            for j in range(i,k,-1):
                s[j]=s[j-1]
            s[k]=tmp
            k+=1
    for i in range(h+1):
        print(s[i],end=" ")
    print()
    
