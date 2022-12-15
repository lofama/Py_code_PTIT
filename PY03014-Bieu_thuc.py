t=int(input())
while t>0:
    t-=1
    a = []
    id = 1
    s=input()
    for i in s:
        if i =='(':
            print(id,end=" ")
            a.append(id)
            id+=1
        elif i == ')':
            print(a[-1],end=" ")
            a.pop()
    print()
