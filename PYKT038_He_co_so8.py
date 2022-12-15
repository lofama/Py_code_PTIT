def doi(s):
    x = len(s)%3
    st = ""
    sum = 0
    for i in range(x):
        sum+= 2**(x-i-1)*int(s[i])
    st = str(sum)
    for i in range(x, len(s),3):
        sum = 0
        for j in range(i,i+3):
            sum+= 2**(2+(i-j))*int(s[j])
        st += str(sum)
    return st
s = input()
print(int(doi(s)))

