dem = 0
m = {}
while True:
    if dem == 10: break
    a = [int(x) for x in input().split()]
    dem+=len(a)
    for i in a:
            m[i%42]=1
print(len(m))
    
    