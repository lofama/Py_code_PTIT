from math import gcd


class PhanSo:
    ts = 0
    ms = 1
    def __init__(self,ts,ms):
        x = gcd(ts,ms)
        self.ts = int(ts/x)
        self.ms = int(ms/x)
    def pr(self):
        print("{}/{}".format(self.ts,self.ms))

a,b,c,d = [int(k) for k in input().split()]
a = a*d+b*c
b = b*d
x = PhanSo(a,b)

x.pr()