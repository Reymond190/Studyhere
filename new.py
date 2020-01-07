# from LatLon.lat_lon import LatLon

date = '140102063807'

# for i in range(0,len(date)+1):
#     if(i%2==0):
#         la = str(date[i-2:i])
#         s = int(la,16)
#         print(s)
#
# ls = '0F'
# a = int(ls,16)
# print(a)

#026B3F3E

# lat = '0899373c'
lat = '089b78f8'
a = lat[0:2]
a1 = int(a,16)
b = lat[2:4]
b1 = int(b,16)
c = lat[4:6]
c1 = int(c,16)
d = lat[6:8]
d1 = int(d,16)

dec = int(lat,16)
float = float(dec)
p1 = float/30000.0   #1352.765

p2 = int(p1/60)  #22

final = p1 - p2*60
print(int(p2))

print(p2,final)

#Degrees (0 to 89, 0 to 179) as integers and minutes (0 to 59.9999)
# Include up to 4 decimal places.


#lat - 12 54.46496666666667
#lon  - 80 13.559199999999691


#--------------------


#lat  - 12 55.34760000000006
#lon   - 80 8.62920000000031


#LatLon


# import reverse_geocoder as rg
# coordinates = ()
# rg.search(coordinates)


# palmyra = LatLon(Latitude(degree = 5, minute = 52), Longitude(degree = -162, minute = -4.998))
# a = LatLon(5.8833, -162.0833)
# print (a.to_string('d%_%M'))


#course status


from geopy.geocoders import Nominatim
# newport_ri = (41.49008, -71.312796)


