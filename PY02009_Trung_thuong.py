t = int(input())
while t>0:
    n = int(input())
    a = {}
    for i in range(n):
        x = int(input())
        if x in a:
            a[x]+=1
        else :
            a[x] = 1
    max = s = 0
    for i in a :
        if a[i] > s :
            s = a[i]
            max = i
        elif a[i] == s :
            max = min(max, i)
    print(max)  
    t-=1