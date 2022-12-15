n = int(input())
k = {}
a={}
for i in range(30000):
    a[i] = 0
# for i in range(n):
k = [int (x) for x in (input().split())]
for i in range (n):
    a[int(k[i])]=1
for i in range(1,30001,1):
    if(a[i]==0):
        print(i)
        break