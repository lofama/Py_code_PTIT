def nto(x):
    x = int(x)
    if x < 2 : return False
    else:
        for i in range(2, x):
            if x % i ==0:
                return False
    return True
n,m = [int(x) for x in input().split()]
for i in range(n):
    a = [int(z) for z in input().split()]
    for i in a:
        if nto(i):
            print(1,end = " ")
        else : 
            print(0,end = " ")
    print()