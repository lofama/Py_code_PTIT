s1 = input()
s2 = input()
vt = int(input())
vt-=1
for i in range(0,vt):
    print(s1[i],end="")
print(s2,end="")
for i in range(vt,len(s1)):
    print(s1[i],end="")