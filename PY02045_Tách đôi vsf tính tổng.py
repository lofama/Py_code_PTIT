s = input()
if len(s)==1:
    print(s)
else:
    while(True):
        if len(s) == 1:
            break
        s1=""
        s2=""
        for i in range(int(len(s)/2)):
            s1 += s[i]
        for i in range(int(len(s)/2),len(s)):
            s2 += s[i]
        s = str(int(s1)+int(s2))
        print(s)
