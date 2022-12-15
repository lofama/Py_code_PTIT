p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while ( True ) :
    ip = input()
    if ip =='0':
        break
    k, s= ip.split()
    kq = ""
    k = int(k)
    for i in s:
        n = 0
        for j in p:
            if i == j:
                break
            n+=1
        x = (k+n)%28
        kq = p[x]+kq
    print(kq)