t = int(input())
while t>0:
    s = input()
    flat = 0
    for i in range(1,len(s),1):
        x = abs(ord(s[i])-ord(s[i-1]))
        y = abs(ord(s[len(s)-i-1])-ord(s[len(s)-i]))
        if x != y:
            flat = 1
            print("NO")
            break
    if flat == 0:
        print("YES")
    t-=1