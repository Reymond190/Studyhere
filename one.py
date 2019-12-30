
# import libscrc

# crc16 = libscrc.modbus(b'1234')
# print(hex('0d010866968031423081000f'))


s = '78780d0108669680314230810009fb880d0a'



p = '78780A134401040001000508450D0A'
print(p[-4:])




l = '78780a130405040002002046240d0a'

sd = '78780a130405040002001cbdcb0d0a'

print('serial --',p[18:22],l[18:22],sd[18:22])



print('lenght ---------',len(l),len(sd),len(p))