n = int(input())
a=['']*n
sum = 0
for i in range(n):
    a[i] = input()
for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C':
            dem+=1
    sum+= int(dem*(dem-1)/2)
for j in range(n):
    dem = 0
    for i in range(n):
        if a[i][j] == 'C':
            dem+=1
    sum+= int(dem*(dem-1)/2)
print(sum)