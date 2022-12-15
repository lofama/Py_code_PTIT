dsNhom=[]
dsTS=[]
class Nhom:
    def __init__(self,id,tent,truong):
        self.ma = 'Team%02d'%int(id)
        self.tent = tent
        self.truong = truong
class SV:
    def __init__(this,id,ten,team):
        this.idSV = 'C%03d'%int(id)
        this.tenSV = ten
        for i in dsNhom:
            if i.ma == team:
                this.tenTeam = i.tent
                this.tenTruong = i.truong
    def xuat(this):
        return this.idSV+" "+this.tenSV+" "+this.tenTeam+" "+this.tenTruong
def cmp(a):
    return a.tenSV

soTeam=int(input())
for i in range(soTeam):
    ma=input()
    ten=input()
    dsNhom.append(Nhom(i+1,ma,ten))

soTS=int(input())
for i in range(soTS):
    ten=input()
    teamm=input()
    dsTS.append(SV(i+1,ten,teamm))
dsTS.sort(key=cmp,reverse=True)
for i in dsTS: print(i.xuat())