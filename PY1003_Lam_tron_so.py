t = int(input())
for k in range(int(t)):
    x = str(input())
    c = 0
    n = len(x)
    for i in range (n-1,0,-1) :

        b = int(x[i]) + c
        if b > 4:
            c = 1
        else:
            c = 0

    a = str(int(x[0])+c)
    print(a,end="")
    for i in range(1,n,1):
        print('0',end='')
    print()