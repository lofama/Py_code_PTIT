s = str(input())
dem = 0
for i in range(0,len(s),1):
    if s[i]>='a':
        if(s[i]<='z'):
            dem+=1
if dem >= len(s)/2:
   s=s.lower() 
else:
    s = s.upper()
print(s)