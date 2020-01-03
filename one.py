
# import libscrc

# crc16 = libscrc.modbus(b'1234')
'''b'7878(startbit)

----------------------------

 1f (len)

----------------------------

 12(protocolno)

------------------------------

13
0c
06
07
33
 2e (date)

-------------------------------

c9(satellites)

------------------------------

01 62 ef  37 (lat)

------------------------------

08
99
42
91(long)

-----------------------------

00(speed)

-----------------------------

54
4c(course status)

----------------------------

01
94(mcc)

00(mnc)

cb
4a(lac)

00
64
a2(cell id)

--------------------------
00
0f(serial_no)

==============
fe
ed(error_check)

==============

0d0a (stop_bit) '''

# 7878 1f12    13 0c 13 07 2f 35   c9    01 62 7c cd    08 9b 79 31    02     5482 0194 00 01f9 00da5f 0011 b533 0d0a


'''

len = s[4:7]

protocolno = s[ 6 : 9 ]


date = s[ 8 : 21 ]

satellites = s[ 20 : 23 ]

lat = s[ 22 : 31 ]

long = s[ 30 : 39 ]

speed = s[ 38 : 41 ]

course_status = s[ 40 : 45 ]

mcc = s[ 44 : 49 ]

mnc = s[ 48 : 51 ]

lac = s[ 50 : 55 ]

cell_id = s[ 54 : 61 ]

serial_no = s[ 60 : 65 ]






'''

sos = '78781f121401020d0c30c90162ed0c0899373c035518019400233e00814400040e820d0a'

s = sos
print(sos.find('.'))

print(sos[:sos.find('.')])

a = sos.find('.')
b = sos.find(',')
print(sos[a+1:b])



len = s[4:6]

protocolno = s[ 6 : 8 ]


date = s[ 8 : 20 ]

satellites = s[ 20 : 22 ]

lat = s[ 22 : 30 ]

long = s[ 30 : 38 ]

speed = s[ 38 : 40 ]

course_status = s[ 40 : 44 ]

mcc = s[ 44 : 48 ]

mnc = s[ 48 : 50 ]

lac = s[ 50 : 55 ]

cell_id = s[ 54 : 60 ]

serial_no = s[ 60 : 64 ]


print('serial_no =','s[',a,':',b,']')


print('len -',len,'__',
      'protocolno',protocolno,'__',
      'date',date,'__',
      'satellites',satellites,'__',
      'lat',lat,'__',
      'long',long,'__',
      'speed',speed,'__',
      'course_status',course_status,'__',
      'mcc ',mcc,'__',
      'mnc ',mnc,'__',
      'lac ',lac,'__',
      'cell_id ',cell_id,'__',
      'serial_no',serial_no,'__')


