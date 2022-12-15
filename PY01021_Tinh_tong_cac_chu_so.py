t = int(input())
while t>0:
    t-=1
    s = input()
    a = [""]*len(s)
    h = 0
    sum = 0
    for i in s:
        if i.isalpha():
            a[h]=i
            h+=1
        else:
            sum+=int(i)
    a.sort()
    for i in a:
        if i!="":
            print(i,end="")
    print(sum)
