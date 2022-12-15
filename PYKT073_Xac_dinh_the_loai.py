# f = open('test.txt', 'r')
t = int(input())
m = []
flag = 0
cau = 0
trc = 0
while t>0:
    t-=1
    s = input().split()
    if(len(s)==7):
        flag = 1
    if flag == 1:
        cau += 1
        if cau == 4:
            m.append(2)
            cau = 0
        flag = 0
    if len(s)==8:
        trc = 8
    if len(s) == 7 and trc == 8:
        m.append(1)
        trc = 7
# f.close()
if trc == 8:
    m.append(1)
print(len(m))
for i in m:
    print(i)