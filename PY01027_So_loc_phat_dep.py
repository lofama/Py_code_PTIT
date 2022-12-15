
def check(t):
    for i in t:
        x = i.split("68")
        for j in x:
            z = j.split("6")
            for k in z:
                if k != '':
                    return False
    return True
t = input().split("688")
if check(t):
    print("YES")
else:
    print("NO") 
