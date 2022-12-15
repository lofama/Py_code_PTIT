a = [i.lower() for i in input().split()]
b = [i.lower() for i in input().split()]
hop = set()
giao = set()
for i in a:
    hop.add(i)
    if i in b:
        giao.add(i)
for i in b:
    hop.add(i)
hop = sorted(hop)
giao = sorted(giao)
for i in hop: print(i,end = " ")
print()
for i in giao: print(i,end=" ")