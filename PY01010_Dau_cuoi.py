t = int(input())
for i in range(t):
    s = str(input())
    if s[0] == s[len(s)-2]:
        if s[1] == s[len(s)-1]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")