def so(s):
    x = int(s)
    for i in range(1000):
        if x%7==0: 
            return x
        else:
            new_str_list = list(reversed(s))
            temp = 0
            for j in range(len(new_str_list)):
                temp = temp*10 + int(new_str_list[j])
            x += temp
            s=str(x)
            # print(new_str_list)
            # new_str = ''.join(new_str_list)
            # x += new_str_list
    return -1

t = int(input())
while t>0:
    s=input()
    print(so(s))
    t-=1