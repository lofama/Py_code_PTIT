def check(s):
    if s[-1].lower() !='y':return False
    if s[-2].lower() !='p': return False
    if s[-3].lower() !='.': return False
    return True
t = input()
if check(t):
    print("yes")
else :
    print("no")
