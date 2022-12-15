def check(s):
    if len(s)<3 : return False
    dem = 0
    for i in range (len(s)-1):
        if int(s[i]) < int(s[i+1]):
            # print(dem,end=", ")
            dem+=1
        else: break
    if dem == len(s) or dem == 0: 
        return False
    else:
        for i in range(dem, len(s)-1,1):
            if int(s[i])<=int(s[i+1]): return False
    return True
t = int(input())
while t>0:
    t-=1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
