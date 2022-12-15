t = int(input())
for i in range (t):
    t-=1
    s1 = sorted(input())
    s2 = sorted(input())
    print("Test " ,i+1,": ", sep="", end="")
    if s1==s2:
        print("YES")
    else: 
        print("NO") 