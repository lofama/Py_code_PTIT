t = int(input())
while t>0:
    t-=1
    n = input()
    sum0 = 0
    sum1 = 0
    tich = 1
    for i in range(len(n)):
        if i%2==0: sum0+=int(n[i])
        else:
            sum1+=int(n[i])
            if int(n[i]) > 0: tich*=int(n[i])
    print(sum0,end=" ")
    if sum1 == 0: print(0)
    else: print (tich)