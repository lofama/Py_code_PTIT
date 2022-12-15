def find(n,k):
   if k == 2**(n-1): return n
   if k > 2**(n-1):return find(n-1,k-2**(n-1))
   return find(n-1,k)
t = int(input())
while t>0:
    t-=1
    n,x = [int(b) for b in input().split()]
    print(chr(find(n,x)+ord('A')-1))