import serial
import pynmea2

port="/dev/ttyS0"
#port="/dev/ttyAMA0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)

def run_gps_lat():
    while True:
        newdata=ser.readline().decode("unicode_escape")
        if newdata[0:6] == "$GPGGA":
            newmsg=pynmea2.parse(newdata)
            lat=newmsg.latitude
            lng=newmsg.longitude
            gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
            print(gps)
            return lat

def run_gps_lng():
    while True:
        newdata=ser.readline().decode("unicode_escape")
        if newdata[0:6] == "$GPGGA":
            newmsg=pynmea2.parse(newdata)
            lng=newmsg.longitude
            return lng


#while True:
    #RunGPSLAT()