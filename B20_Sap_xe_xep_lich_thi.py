mon={}
with open('MONTHI.in','r') as fmon:
    so = int(fmon.readline())
    for i in range(so):
        ma = fmon.readline().rstrip('\n')
        ten = fmon.readline().rstrip('\n')
        ht = fmon.readline().rstrip('\n')
        mon[ma]=[ten]
fmon.close()
cathi=[]
with open('CATHI.in','r') as fca:
    soca = int(fca.readline())
    cathi=[""]*soca
    for i in range(soca):
        tg=""
        ngay = fca.readline().rstrip('\n')
        x = ngay.split("/")
        tg = str(x[2])+"/"+str(x[1])+"/"+str(x[0])+ " "
        gio = fca.readline().rstrip('\n')
        phong = fca.readline().rstrip('\n')
        tg += gio+" "+ phong
        cathi[i]=tg
fca.close()
solich = 0
with open('LICHTHI.in','r') as flich:
    solich = int(flich.readline())
    for i in range(solich):
        maca,mam,x,y = flich.readline().split()
        cathi[i] = str(maca)+" "+cathi[i]
        cathi[i] = str(mam)+" "+cathi[i]
        cathi[i]+=" " + str(maca)
        print(cathi[i])
        
        for j in mon[mam]:
            cathi[i]+=" "+str(j)
        cathi[i]+=" " + str(x)
        cathi[i]+=" " + str(y)
flich.close()
cathi.sort()
# print(cathi)
for z in range(solich):
    i = cathi[z]
    j = i.split()
    x = j[2].split("/")
    tg = str(x[2])+"/"+str(x[1])+"/"+str(x[0])
    j[2]=tg        
    for k in range(2,len(j)):
        if(k!=5):
            print(j[k],end = " ")
    print()