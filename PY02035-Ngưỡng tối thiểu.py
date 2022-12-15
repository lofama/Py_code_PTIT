a = input()
b = int(input())
c = {}
n = int(len(a)/2)*2
for i in range(0,n,2):
    x = int(a[i])*10+int(a[i+1])
    if x not in c: 
        c[x] = 1
    else:
        c[x]+=1
dem = 0
for i in sorted(c):
    if c[i] >= b:
        print(str(i)+" "+str(c[i]))
        dem+=1
if dem == 0:
    print("NOT FOUND")
