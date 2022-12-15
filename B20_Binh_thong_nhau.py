q = int(input())
m=[]
while q > 0:
    q-=1
    s = input().split()
    if s[2]=="1":
        if len(m)==0:
            m.append(s[0])
            m.append(s[1])
            continue
        if s[0] in m or s[1] in m :
            m.append(s[0])
            m.append(s[1])
            for i in m:
                if "." in i and (s[0] in i or s[1] in i):
                    print(16)
                    for z in i.split("."):
                        m.append(z)
        else:
            dem = 0
            for i in range (len(m)):
                if "." in m[i]:
                    dem+=1
                    x = m[i].split(".")
                    if s[0] in x:
                        print(24)
                        for j in range(i,len(m)):
                            if "." in m[j]:
                                x1 = m[j].split(".")
                                if s[0] in x1 or s[1] in x1:
                                    m[i] = m[i]+"."+m[j]
                        m[i]=m[i]+"."+s[1]
                    else:
                        if s[1] in x:
                            m[i]=m[i]+"."+s[0]
                        else:
                            st = s[0]+"."+s[1]
                            m.append(st)
                            print(37)
            if dem == 0:
                st = s[0]+"."+s[1]
                m.append(st)
                print(43)
        m.sort()
        print(m)

    else:
        if s[0] in m and s[1] in m:
            print(1)
        else:
            flag = 1
            for i in m:
                if "." in i and (s[0] in i and s[1] in i):
                    print(1)
                    flag = 0
                    break
            if flag == 1:
                print(0)
            
            
