a = {}
def check(x):
    while True:
        if x%2>0: break
        x = x/2
    while True:
        if x%3>0: break
        x= x/3
    while True:
        if x%5>0: break
        x = x/5
    if x > 1: return False
    return True 
j = 0
for i in range(1,10000000):
    if check(i): 
        a[j] = i
        j+=1
t = int(input())
while t>0:
    t-=1
    j = 0
    n = int(input())
    if check(n):
        for i in range(1,n+1):
            if check(i):
                j+=1
        print(j)
    else: print("Not in sequence")