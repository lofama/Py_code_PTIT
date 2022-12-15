m = {}
def sum(s):
    sum = 0
    for i in s:
        sum+=int(i)
    return sum
t = int(input())
while t>0:
    t-=1
    n = int(input())
    a =[str(x) for x in input().split()]
    for i in range(len(a)):
        for j in range(i,len(a)):
            if(sum(a[i])>sum(a[j])):
                tmp = a[i]
                a[i]=a[j]
                a[j]=tmp
            if(sum(a[i])==sum(a[j])) and int(a[i])>int (a[j]):
                tmp = a[i]
                a[i]=a[j]
                a[j]=tmp
    for i in a:
        print(i,end=" ")
    print()