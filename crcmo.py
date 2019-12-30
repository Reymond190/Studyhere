import crcmod
import binascii


#mystr = {'9ebe':'0d010866968031423081000f','31e4':0d0108669680314230810005','0d0108669680314230810003','0d0108669680314230810005'}
mystr = '0d0108669680314230810005'
ret1 = str.encode(mystr)

xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=True, initCrc=0x0000, xorOut=0xFFFF)
#print(hex(xmodem_crc_func(b'\r\x01\x08f\x96\x801B0\x81\x00\x0f')))
ai = xmodem_crc_func(binascii.unhexlify(ret1))
print('unhexlified', binascii.unhexlify(ret1))
final_ec = hex(ai)
print('ai',final_ec)




