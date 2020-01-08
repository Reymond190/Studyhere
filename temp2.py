
#'78780813 4B 04 03 00 01 0011061F0D0A'

#4B 04 030001








heartbeat = '787808134B040300010011061F0D0A'
    #reqbeat = heartbeat[8:18]

he = "b'78781f121401080a2505c701627cc8089b7baa00542501940001f900da5f0019bd0a0d0a'"

print(len(he))
p = he[1::]
p = p.replace("'", "")
print(p)


s = p
len = s[4:6]
protocolno = s[6: 8]
date = s[8: 20]
satellites = s[20: 22]
lat = s[22: 30]
long = s[30: 38]
speed = s[38: 40]
course_status = s[40: 44]
mcc = s[44: 48]
mnc = s[48: 50]
lac = s[50: 54]
cell_id = s[54: 60]
serial_no = s[60: 64]







print('len -', len, '__',
'protocolno', protocolno, '__',
'date', date, '__',
 'satellites', satellites, '__',
 'lat', lat, '__',
  'long', long, '__',
                  'speed', speed, '__',
                  'course_status', course_status, '__',
                  'mcc ', mcc, '__',
                  'mnc ', mnc, '__',
                  'lac ', lac, '__',
                  'cell_id ', cell_id, '__',
                  'serial_no', serial_no, '__')
