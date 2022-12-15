s = input()
b = (len(s)-1)%3
if b == len(s) - 1: b = -1
for i in range(len(s)):
    print(s[i],end="")
    if i == b and b != len(s)-1:
        print(",",end="")
        b+=3