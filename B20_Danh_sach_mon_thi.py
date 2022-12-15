t = int(input())
a = [""]*t
for i in range(t):
    for j in range(3):
        a[i]+=input()+" "
a.sort()
for i in a:
    print(i)