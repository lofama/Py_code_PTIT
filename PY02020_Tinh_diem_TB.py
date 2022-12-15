t = int(input())
a = [float(x) for x in input().split()]
ma = max(a)
mi = min(a)
dem =0
sum = 0
for i in a:
    if i>mi and i<ma:
        sum+=i
        dem+=1
print("{:.2f}".format(sum/dem))
