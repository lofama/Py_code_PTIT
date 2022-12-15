x = int(input())
for a in range (x):
    n = str(input())
    dem = 0
    for i in range(len(n)):
        if int(n[i])==4 :
            dem+=1
        if int(n[i])==7 :
            dem+=1
    if dem == len(n):
        print("YES")
    else :  
        print("NO")