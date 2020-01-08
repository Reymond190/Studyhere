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





def date(value):
    year = value[0:2]
    month = value[2:4]
    day = value[4:6]
    hour = value[6:8]
    minute = value[8:10]
    second = value[10:12]

    year = int(year, 16)
    month = int(month, 16)
    day = int(day, 16)
    hour = int(hour, 16)
    minute = int(minute, 16)
    second = int(second, 16)



    year = "20"+str(year)
    result = str(day)+'-'+str(month)+'-'+str(year)+' '+str(hour)+':'+str(minute)+':'+str(second)
    print('result',result)


print(date('1401020d0c30'))


def mcc(val):
    dec = int(val, 16)
    print('mcc',dec)




#'78780813 4B 04 03 00 01 0011061F0D0A'

#4B 04 030001

heartbeat = '787808134B040300010011061F0D0A'
reqbeat = heartbeat[8:18]




def status_packet(value):

    my_hexdata1 = value[0:2]                #terminal information content
    my_hexdata2 = value[2:4]                #battery/voltage level
    my_hexdata3 = value[4:6]                #gsm signal status
    my_hexdata4 = value[6:8]                #alarm status
    my_hexdata5 = value[8:10]               #language
    print((my_hexdata2))

    #---------------continue from here----------------


    scale = 16  ## equals to hexadecimal
    num_of_bits = 8

    p = bin(int(my_hexdata1, scale))[2:].zfill(num_of_bits)
    # q = bin(int(my_hexdata2, scale))[2:].zfill(num_of_bits)

    print(p)

    last = p
    count = 0

    # endcourse = endval
    gpssta = ''
    pos  = ''
    londir = ''
    charge = ''
    acc = ''
    vat = ''
    var = ''




    for i in last:
        count+=1
        if (count == 1):
            if(i=='0'):
                gpssta = 'gas oil and electricity connected'
                print('gas oil and electricity')
            else:
                gpssta = 'oil and electricity disconnected'
                print('oil and electricity disconnected')
        elif (count == 2):
            if(i == '0'):
                pos = 'GPS tracking is off'
            else:
                pos = 'GPS tracking is on'

        elif(count >= 3 and count <=5):
            var += i
            if(count == 5 and len(var) == 3):
                if(var == '100'):
                    londir = 'SOS'
                elif(var == '011'):
                    londir = 'Low Battery Alarm'
                elif(var == '010'):
                    londir = 'Power Cut Alarm'
                elif (var == '001'):
                    londir = 'Shock Alarm'
                elif (var == '000'):
                    londir = 'Normal'

        elif(count==6):
            if (i == '0'):
                charge = 'Charge Off'
            else:
                charge = 'Charge On'

        elif(count == 7):
            if(i=='0'):
                acc = 'ACC Low'
            else:
                acc = 'ACC high'

        elif (count == 8):
            if (i == '0'):
                vat = 'Deactivated'
            else:
                vat = 'Activated'


    dict = {'gpsstatus':gpssta,'GPS tracking':pos,'alarm':londir,'charge':charge,'ACC':acc,'gps':vat}

    #-----------------------------------------------------------------------------------------------
    voltval = ''

    voltlev = str(my_hexdata2)
    print('is this',voltlev)

    if(voltlev == '00'):
        #print('no power')
        voltval = 'No Power (shutdown)'
    elif (voltlev == '01'):
        #print('Extremely Low Battery')
        voltval = 'Extremely Low Battery'
    elif (voltlev == '02'):
        #print('Very Low Battery')
        voltval = 'Very Low Battery'
    elif (voltlev == '03'):
        #print('Extremely Low Battery')
        voltval = 'Low Battery'
    elif (voltlev == '04'):
        #print('Extremely Low Battery')
        voltval = 'Medium'
    elif (voltlev == '05'):
        # print('Extremely Low Battery')
        voltval = 'High'
    elif (voltlev == '06'):
        # print('Extremely Low Battery')
        voltval = 'Very High'

    #------------------------------------------------------------------------------------------------------------------
    gsmlev = str(my_hexdata3)
    gsmval = ''

    if (gsmlev == '00'):
        # print('no power')
        gsmval = 'no signal'
    elif (gsmlev == '01'):
        # print('Extremely Low Battery')
        gsmval = 'extremely weak signal'
    elif (gsmlev == '02'):
        # print('Very Low Battery')
        gsmval = 'very weak signal'
    elif (gsmlev == '03'):
        # print('Extremely Low Battery')
        gsmval = 'good signal'
    elif (gsmlev == '04'):
        # print('Extremely Low Battery')
        gsmval = 'strong signal'

    alarmlang = str(my_hexdata4)
    alarmlang1 = str(my_hexdata4)
    alarmlang2 = str(my_hexdata5)

    #------------------------------------------
    almmsg = ''

    if (alarmlang1 == '00'):
        # print('no power')
        almmsg = 'normal'
    elif (alarmlang1 == '01'):
        # print('Extremely Low Battery')
        almmsg = 'SOS'
    elif (alarmlang1 == '02'):
        # print('Very Low Battery')
        almmsg = 'Power Cut Alarm'
    elif (alarmlang1 == '03'):
        # print('Extremely Low Battery')
        almmsg = 'Shock Alarm'
    elif (alarmlang1 == '04'):
        # print('Extremely Low Battery')
        almmsg = 'Fence In Alarm'

    elif (alarmlang1 == '05'):
        # print('Extremely Low Battery')
        almmsg = 'Fence Out Alarm'


        #break
        almmsg2 = ''

    if (alarmlang2 == '01'):
        # print('Extremely Low Battery')
        almmsg2 = 'Chinese'

    elif (alarmlang2 == '02'):
        # print('Extremely Low Battery')
        almmsg2 = 'English'


    redic = {'terminal_information':dict,'voltage level':voltval,'gsm signal strength': gsmval,'Alarm':almmsg,'language':almmsg2}

    return redic




