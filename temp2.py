
#'78780813 4B 04 03 00 01 0011061F0D0A'

#4B 04 030001








heartbeat = '787808134B040300010011061F0D0A'
    #reqbeat = heartbeat[8:18]


print(len(heartbeat))



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


def fun_satellites(value):
    return