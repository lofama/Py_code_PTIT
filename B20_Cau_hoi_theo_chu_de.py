t = int(input())
dem = 0
for i in range(t):
    if dem == t:
        break
    x = input()
    dem+=1
    cau=0
    while True:
        if dem ==t:
            print(x,end =": ")
            print(cau)
            break
        s = input()
        if s!="":
            cau+=1
            dem+=1
        else:
            dem+=1
            print(x,end =": ")
            print(cau)
            break
