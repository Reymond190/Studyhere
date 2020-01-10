import datetime

import pytz


time2 = datetime.datetime.now()
tz = pytz.timezone('Asia/Kolkata')
time2 = time2.astimezone(tz)
dt = time2.strftime("%d-%m-%Y %H:%M:%S")
print(dt)