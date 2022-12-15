from re import X


def tim(n):
    a = '012'
    x = 1
    dem = 0
    while True:
        str1 =""
        b = x
        x+=1
        de = 0
        while b > 0:
            str1 = str(a[b%3]) + str1
            b = int(b/3)
        for i in str1:
            if i =='2': 
                de += 1
        if de > int(len(str1)/2):
            print(str1,end=", ")
            dem+=1
        if dem == n:
            break
        
t = int(input())
while t>0:
    t-=1
    n = int(input())
    tim(n)
    print()
