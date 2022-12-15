from re import X


dsLoai={}
dsKH=[]
dsLoai['A']=100
dsLoai['B']=500
dsLoai['C']=100
class KH:
    def __init__(this,id,ten,loai,dau,cuoi):
        this.idKH = 'KH%02d'%(id)
        s = ten.lower().split("/s+")
        x = ""
        for i in s:
            i = i.title()
            x = x + " "+i
        x = x.strip()
        this.tenKH = x
        han = dsLoai[loai]
        so = int(cuoi)-int(dau)
        if so<han:
            this.Trong = so*450
            this.Vuot = 0
        else:
            this.Trong = han*450
            this.Vuot = (so-han)*1000
        this.VAT = int(this.Vuot/20)
        this.nop = this.Trong+this.Vuot+this.VAT
    def xuat(this):
        return str(this.idKH)+" " +str(this.tenKH)+" "+str(this.Trong)+" "+str(this.Vuot)+" "+str(this.VAT)+" "+str(this.nop)
def cmp(a):
    return a.nop
n = int(input())
for i in range(n):
    ten = input()
    l, d, c = input().split()
    dsKH.append(KH(i+1,ten,l,d,c))
dsKH.sort(key=cmp,reverse=True)
for i in dsKH:
    print(i.xuat())
