def sum1(N):
    s = 0.0
    for i in range(1,N+1,2):
        s+=1/i
    return s
def sum0(N):
    s = 0.0
    for i in range(2,N+1,2):
        s+=1/i
    return s

t = int(input())
while t>0:
    t-=1
    n = int(input())
    if n%2 == 0:
        print( "{:.6f}".format(sum0(n)))
    else:
        print("{:.6f}".format(sum1(n)))