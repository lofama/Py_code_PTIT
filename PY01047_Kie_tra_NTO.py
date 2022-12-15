def nto(x):
    x = int(x)
    if x < 2 : return False
    else:
        for i in range(2, x):
            if x % i ==0:
                return False
    return True
def check(s):
    sum=0
    if len(s) <= 4: sum = int(s)
    else:
        for i in range(len(s)-4,len(s),1):
            sum=sum*10 + int(s[i])
    return nto(sum)    

t = int(input())
while t>0:
    s = input()
    if(check(s)): 
        print("YES")
    else: 
        print("NO")
    t-=1