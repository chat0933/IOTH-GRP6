import zmq
import time
import json
from gps import run_gps_lat, run_gps_lng
from imu import run_imu



context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


fallen_variable = run_imu() # Dette skal være = data fra IMU som returner True
heart_variable = 89 # Dette ville være statisk så længe vi ikke har ekg
gps_lat_variable = run_gps_lat() # Dette skal være = data fra GPS so retunerer lat værdi
gps_lng_variable = run_gps_lng() # Dette skal være = data fra GPS so retunerer lng værdi


json_data = {
    #"id" : 1,
    "FALLEN": fallen_variable, 
    "HEARTH_RATE": heart_variable,
    "gpslat" :  gps_lat_variable,
    "gpslng" :  gps_lng_variable   
}


def send_rpi_data():
    try:
        #for times in range(2):
        test_number = 0 # DETTE SKAL VÆRE IMU X,Y,Z ACCELRATION ELLER X
        while True:
            if test_number == 0:  # DETTE SKAL VÆRE IMU X,Y,Z ACCELRATION ELLER X
                #message = f"Danger"#{times}"  #Beskeden her skal afgøres af enten IMU eller EKG
                #print(f"Sending: {message}")
                #Prøv måske at tage nogle statiske værdier på det hele og så send det for at se om RPi kan bruge dem 
                print("Trying to send Json data")
                message = json.dumps(json_data)
                print(message)
                #socket.send_string(message)
                socket.send_string(message)
                #socket.send_string(json_message)
                time.sleep(5)
                    #test_number = test_number+1
            
            # Kan også godt være else
            """
            elif test_number == 1:  # DETTE SKAL VÆRE IMU X,Y,Z ACCELRATION ELLER X
                message = f"Dange"#{times}"  #Beskeden her skal afgøres af enten IMU eller EKG
                print(f"Sending: {message}")
                socket.send_string(message)
                time.sleep(5) 
                #test_number = test_number -1
            """
    except KeyboardInterrupt:
        socket.close()
        context.term()
        #socket.disconnect()
        #socket.send_string("Hello, ZeroMQ!")

send_rpi_data()