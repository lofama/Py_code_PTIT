t = int(input())
while t>0:
    t-=1
    a = int(input())
    dem = 0
    for i in range(2,int(a/2)+1,1):
        # if i > a:break 
        if i%2 == 0:
            if (a-i/2)%i == 0:
                # chk = int((a-i/2)/i)
                # if chk > int((a-i/2)/chk):break
                dem+=1
        else:
            if a%i==0:
                # if int(a/i) < i:break
                dem+=1
    print(dem)