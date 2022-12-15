t = int(input())
while t>0:
    t-=1
    c,d = [int(x) for x in input().split()]
    if c<d :
        tmp = d
        d = c
        c=tmp
    a = input().strip()
    if(a.count(' ')) : a, b = a.split()
    else : b = input()
    sum1 = 0
    sum2 = 0
    for i in a:
        if int(i) == c:
            sum1 = 10*sum1+d
        else:
            sum1 = 10*sum1+int(i)
    for i in b:
        if int(i) == c:
            sum2 = 10*sum2+d
        else:
            sum2 = 10*sum2+int(i)
    print(sum1+sum2,end = " ")
    sum1 = 0
    sum2 = 0
    for i in a:
        if int(i) == d:
            sum1 = 10*sum1+c
        else:
            sum1 = 10*sum1+int(i)
    for i in b:
        if int(i) == d:
            sum2 = 10*sum2+c
        else:
            sum2 = 10*sum2+int(i)
    print(sum1+sum2)
        
