t = int(input())
for a in range(t) :

    def check(x):
        if x % 2 != 0 :
            return False
        s = str(x)
        for i in range(int(len(s)/2)+1):
            if(int(s[i])!=int(s[len(s)-1-i])):
                return False
            if(int(s[i])%2!=0) :
                return False
        return True
    


    n = int(input())
    for i in range(22, n, 2 ) :
        a = i
        if check(i):
            print(a , end=" ")
    
    print()