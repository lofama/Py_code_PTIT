t=int(input())
while t > 0:
    t-=1
    n,k = [int(x) for x in input().split()]
    s = input().split()
    for i in range (k,n):
        print(s[i],end = " ")
    for i in range(k):
        print(s[i], end=" ")
    print()