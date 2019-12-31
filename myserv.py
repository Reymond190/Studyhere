import socket               # Import socket mod
import _thread
import binascii
import struct
import sys
from crc_itu import crc16
import libscrc



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
        #l = 'LOAD'
        #p = hex(crc16(imei))
        str_data = str(imei)
        print('01',str_data[8:10])
        if str_data[8:10] == '01':
                parsed_data = str_data[26:30]
                first_data = str_data[2:6]    #7878
                length = '0501'
                #print('first-data', first_data)
                #print('length', length)
                #print('parsed-data', parsed_data)
                #p = str(p)
                #s = p[2:6]
                error_check =  'ECHE'
                #print('error_check - ',error_check)
                strink = first_data+length+parsed_data+error_check+'0d0a'
                ret1 =  str.encode(strink)
                #print('pre_output',ret1)
                mystr = strink[4:12]
                #print(mystr)
                ret1 = str.encode(mystr)
                crc16 = libscrc.x25(binascii.unhexlify(ret1))
                ra = hex(crc16)
                #print('pre_errorc', ra)
                ra = str(ra)
                error_check = ra[2:6]
                #print('final_error',error_check)
                strink = first_data+length+parsed_data+error_check+'0d0a'
                print('final_string',strink)
                ret2 = str.encode(strink)
                print(type(ret2))
                print(ret2)
                ret1 = binascii.unhexlify(ret2)
                #print('crc-',hex(crc16(ret1)))
                print('ret - ',ret1)
                print('ret type - ',type(ret1))
                clientsocket.send(ret1)
        elif str_data[8:10] == '13':
            first_data = str_data[2:6]
            last = '0a0d'
            print('first-data',first_data)
            len = '0513'
            print('length',len)
            serial_no = str_data[18:22]
            print('serial_no',serial_no)
            final = len+serial_no
            re = str.encode(final)
            crc16 = libscrc.x25(binascii.unhexlify(re))
            ra = str(hex(crc16))
            error_check = ra[2:6]
            print('errror_check',error_check)
            finalout = first_data+final+error_check+last
            print('final', finalout)
            ret2 = str.encode(finalout)
            print('encode',ret2)
            ret1 = binascii.unhexlify(ret2)
            print('ret - ', ret1)
            print('ret type - ', type(ret1))
            clientsocket.send(ret1)
        # elif str_data[8:10] == '13':
        #     first_data = str_data[2:6]
        #     last = '0a0d'

        else:
            print('something new----',str_data)
            print('closing connection....')
            clientsocket.close()
 except socket.error as message:
  print(message)
  clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()  # Get local machine name
print(host)
port = 49153                 # Reserve a port for your service.

print('Server started!')
print(sys.stderr, '\nwaiting for a connection')

s.bind((host, port))        # Bind to the port
s.listen(5)     # Now wait for client connection.
unpacker = struct.Struct('I 2s f')


while True:
   c, addr = s.accept()     # Establish connection with client.
   _thread.start_new_thread(on_new_client,(c,addr))
   print('got connected by ',addr)
s.close()


