def tinh(s):
    sum = 0
    for i in s:
        sum+=ord(i)-ord('0')
    a = str(sum)
    return a
t = input()
dem = 0
while(len(t)>1):
    t = tinh(t)
    dem += 1
print(dem)
