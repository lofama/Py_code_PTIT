while True:
    n = int(input())
    if n == 0:
        break
    dem = 1
    while True:
        if n == 1: 
            break
        if n%2==0:
            n=n/2
        else:
            n = n*3+1
        dem+=1
    print(dem)