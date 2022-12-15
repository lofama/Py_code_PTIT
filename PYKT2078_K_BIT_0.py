import math
h2 = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648]
t = int(input())
while t>0:
    t-=1
    dem  = 0
    n,k = [int(x) for x in input().split()]
    dai = 1 + int(math.log(n)/math.log(2))
    check = 2**dai-2*(dai-1)
    while(True):
        if sum >= check :
            dem+=1
        sum = 0
        s = k
        while(True):
            s-=1
            

