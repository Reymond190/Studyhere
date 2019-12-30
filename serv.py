import socket               # Import socket mod
import _thread
import binascii
import struct
import sys
from crc_itu import crc16



def on_new_client(clientsocket,addr):
 try:
    while True:
       # msg = clientsocket.recv(2024)
       # print('connected by',addr)
        data = clientsocket.recv(5000)
        print (sys.stderr, 'received raw "%s"' ,data)
        print('type raw:',type(data))
        #unpacked_data = unpacker.unpack(data)
        #print(sys.stderr, 'unpacked:', unpacked_data)
        #m = str(msg)
        #print('message',m)
        imei = binascii.hexlify(data)
        imei2 = "null"
        print('data hexlified - ',imei)
        print('type',type(imei))
        print('data ascii ed - ',imei2)
        print('type',type(imei2))
        l = 'LOAD'
        p = hex(crc16(imei))
        str_data = str(imei)
        parsed_data = str_data[26:30]
        first_data = str_data[2:6]
        length = '0501'
        print('first-data', first_data)
        print('length', length)
        print('parsed-data', parsed_data)
        p = str(p)
        s = p[2:6]
        s = str(s)
        print(p)
        print(s)
        #ret = binascii.unhexlify(l)
        ret1 =  str.encode(first_data+length+parsed_data+s+'0d0a')
        print('final output',ret1)
        ret2 = str.encode('LOAD')
        ret1 = binascii.unhexlify(ret1)
        #print('crc-',hex(crc16(ret1)))
        print('ret - ',ret1)
        print('ret type - ',type(ret1))
        clientsocket.send(ret1)
        clientsocket.close()
 except socket.error as message:
  print(message)
  clientsocket.close()



import libscrc
import binascii

mystr = '0d010866968031423081000f'
ret1 = str.encode(mystr)
crc16 = libscrc.x25(binascii.a2b_hex('0d010866968031423081000f'))
print('binascii', binascii.a2b_hex('0d010866968031423081000f'))
print('unhexlify', ret1=binascii.unhexlify(ret1))
print(crc16)
ans2 = libscrc.x25(b'0d010866968031423081000f')
print('ans input as string', ans2)




