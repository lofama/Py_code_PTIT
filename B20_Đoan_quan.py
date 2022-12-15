t= int(input())
while t>0:
    t-=1
    n = int(input())
    mc=[]
    vt = [int(x) for x in input().split()]
    h = [int(a) for a in input().split()]
    q = int(input())
    mc.append(int(h[0]*vt[0]))
    for i in range(1,n):
        s=0
        j = i-1
        while True:
            if j < 0 or h[j]>=h[i]:
                break
            else: j-=1
        if j < 0:
            tru = 0
            for z in range(0,i):
                tru += h[z]
            s = h[i]*vt[i]-tru
        else:
            tru1 = 0
            for z in range (j+1,i):
                tru+=h[z]
            s = int(mc[j])+(vt[i]-vt[j]-1)*h[i]-tru1
        mc.append(s)
    # print(mc)
    while q > 0:
        q-=1
        k = int(input())
        for i in range(n):
            if k <= mc[i]:
                print(i)
                break
            if k > mc[n-1]:
                print(n)
                break