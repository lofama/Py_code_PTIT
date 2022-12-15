def check(s):
    sum = 1
    for i in range(len(s)):
        if int(s[i]) > 0:
            sum *=int(s[i])
    return sum

t = int(input())
while t>0:
    s = input()
    print(check(s))
    t-=1