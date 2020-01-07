import binascii

lat = '089b78f8'

def latloncalc(lat):
    if (len(lat) != 8):
        print('wrong values')

    else:
        print('value is correct')
        # a = lat[0:2]
        # a1 = int(a, 16)
        # b = lat[2:4]
        # b1 = int(b, 16)
        # c = lat[4:6]
        # c1 = int(c, 16)
        # d = lat[6:8]
        # d1 = int(d, 16)
        dec = int(lat, 16)
        flo = float(dec)
        p1 = flo / 30000.0  # 1352.765

        p2 = int(p1 / 60)  # 22

        final = p1 - p2 * 60
        print(int(p2))
        print('dmm',p2, final)
        mins = final/60
        decimal_degrees = p2 + mins
        decimal_degrees = round(decimal_degrees,5)
        print('dd', decimal_degrees)

# latloncalc(lat)



def seperation(datastring):
    if (len(datastring) == '72'):
        s= datastring
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

        lac = s[50: 55]

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

        datavalue = {"len":len,"protocolno":protocolno,'date':date,'satellites':satellites,
                     'lat':lat,'long':long,'speed':speed,'course_status':course_status,
                     'mcc':mcc,'mnc':mnc,'lac':lac,'cell_id':cell_id,'serial_no':serial_no}

        return datavalue



def speedcalc(value):
    dec = int(value, 16)
    print(dec)






def course_status(value):
    # hex_to_binary('abc123efff')
    # print(binary_string)
    # p = format(value, '0>42b')
    # print(p)
    my_hexdata1 = value[0:2]
    my_hexdata2 = value[2:4]

    scale = 16  ## equals to hexadecimal

    num_of_bits = 8

    p = bin(int(my_hexdata1, scale))[2:].zfill(num_of_bits)
    q = bin(int(my_hexdata2, scale))[2:].zfill(num_of_bits)
    print(p,q)

    p = str(p)
    q = str(q)

    last = p+q

    print(last)
    count = 0
    course = last[6:]

    if(len(course)== 10):
        endval = int(course, 2)
    else:
        endval = 0
        print('check the string')

    endcourse = endval
    gpssta = ''
    pos  = ''
    londir = ''
    latdir = ''





    for i in last:
        count+=1
        if (count == 3):
            if(i=='0'):
                gpssta = 'real-time'
                print('real-time gps')
            else:
                gpssta = 'differential positioning'
                print('differential posttioning gps')
        elif (count == 4):
            if(i == '0'):
                pos = 'not positioned'
            else:
                pos = 'positioned'

        elif(count == 5):
            if(i == '0'):
                londir = 'east'
            else:
                londir = 'west'

        elif(count == 6):
            if(i=='0'):
                latdir = 'south'
            else:
                latdir = 'north'


    dict = {'gpsstatus':gpssta,'positioning':pos,'londirection':londir,'latdirection':latdir,'direction':endcourse}
    print(dict)








def mcc(val):
    dec = int(val, 16)
    print('mcc',dec)




#'78780813 4B 04 03 00 01 0011061F0D0A'

#4B 04 030001

heartbeat = '787808134B040300010011061F0D0A'
reqbeat = heartbeat[8:18]

def status_packet(value):

    my_hexdata1 = value[0:2]
    my_hexdata2 = value[2:4]                #battery status
    my_hexdata3 = value[4:6]                #gsm signal status
    my_hexdata4 = value[6:8]                #alarm status
    my_hexdata5 = value[8:10]               #language


    #---------------continue from here----------------


    scale = 16  ## equals to hexadecimal

    num_of_bits = 8

    p = bin(int(my_hexdata1, scale))[2:].zfill(num_of_bits)
    q = bin(int(my_hexdata2, scale))[2:].zfill(num_of_bits)
    print(p,q)

    p = str(p)
    q = str(q)

    last = p+q

    print(last)
    count = 0
    course = last[6:]

    if(len(course)== 10):
        endval = int(course, 2)
    else:
        endval = 0
        print('check the string')

    endcourse = endval
    gpssta = ''
    pos  = ''
    londir = ''
    latdir = ''





    for i in last:
        count+=1
        if (count == 3):
            if(i=='0'):
                gpssta = 'real-time'
                print('real-time gps')
            else:
                gpssta = 'differential positioning'
                print('differential posttioning gps')
        elif (count == 4):
            if(i == '0'):
                pos = 'not positioned'
            else:
                pos = 'positioned'

        elif(count == 5):
            if(i == '0'):
                londir = 'east'
            else:
                londir = 'west'

        elif(count == 6):
            if(i=='0'):
                latdir = 'south'
            else:
                latdir = 'north'


    dict = {'gpsstatus':gpssta,'positioning':pos,'londirection':londir,'latdirection':latdir,'direction':endcourse}
    print(dict)




