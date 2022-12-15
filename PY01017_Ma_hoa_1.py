t = int(input())
while t >0:
    s = input()
    dem = 1
    for i in range(0,len(s)-1,1):
        if s[i]==s[i+1] :
             dem+=1
        else:
            print(dem,end = "")
            print(s[i],end = "")
            dem = 1
    print(dem,end="")
    print(s[len(s)-1])
    t-=1