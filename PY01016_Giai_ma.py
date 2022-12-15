t = int(input())
for m in range(t):
    s=input()
    for m in range(1,len(s),2):
        for x in range(int(s[m])):
            print(s[m-1],end="")
    print()