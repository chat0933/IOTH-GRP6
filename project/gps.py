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

"""
import serial
import pynmea2
from time import sleep


port="/dev/ttyS0"
#port="/dev/ttyAMA0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)

tal = 1

def RunGPSLAT():
    #test_time= 1
    try:
        #while True:
        newdata=ser.readline().decode("unicode_escape")
        #newdata=ser.readline().decode("utf-8")
        if newdata[0:6] == "$GPGGA":
            newmsg=pynmea2.parse(newdata)
            lat=newmsg.latitude
            lng=newmsg.longitude
            gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
            print(gps)
            #print("TEST 3")
            sleep(3)
            return lat
    except UnicodeDecodeError as e:
        print(f"Error decoding: {e}")

def RunGPSLNG():
    while True:
        #newdata=ser.readline().decode("utf-8")
        #newdata=ser.readline().decode("unicode_escape")
        sleep(2)
        if newdata[0:6] == "$GPGGA":
            newmsg=pynmea2.parse(newdata)
            lng=newmsg.longitude
            return lng


while True:
    RunGPSLAT()
    
    if tal == 1:
        print("starter GPS")
        tal = tal+ 1
    elif tal == 2:
        RunGPSLAT()
        RunGPSLNG()
"""