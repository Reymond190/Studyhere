


date = '140102063807'

for i in range(0,len(date)+1):
    if(i%2==0):
        la = str(date[i-2:i])
        s = int(la,16)
        print(s)

ls = '0F'
a = int(ls,16)
print(a)