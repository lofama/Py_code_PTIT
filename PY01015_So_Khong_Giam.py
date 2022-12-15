t = int(input())
for m in range(t):
    x = input()
    flat = 0
    for i in range(len(x)-1):
        if int(x[i])>int(x[i+1]):
            print("NO")
            flat = 1
            break
    if flat == 0 :
        print("YES")
