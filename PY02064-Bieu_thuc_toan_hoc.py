from re import S


t = int(input())
while t>0:
    t-=1
    sum=0
    ans = -10**10
    n,k = [int(x) for x in input().split()]
    a = [int(z) for z in input().split()]
    for i in range(0,n-4):
        sum = 0
        for j in range(1,k+1):
            s=a[i+5*(j-1)]-2*a[i+1+5*(j-1)] +3*a[i+2+5*(j-1)]-4*a[i+3+5*(j-1)]+5*a[i+4+5*(j-1)]
            sum += s
            print(s)
        ans = max(sum,ans)
    print(ans)