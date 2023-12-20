import zmq
import time
import json
from gps import RunGPSLAT, RunGPSLNG
from imu import run_imu

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

def send_rpi_data():
    try:
        while True:
            imu_data = run_imu()
            if imu_data == "imu_danger":
                
                fallen_variable = "True" # Dette skal være = data fra IMU som returner True
                heart_variable = 89 # Dette ville være statisk så længe vi ikke har ekg
                gps_lat_variable = RunGPSLAT() # Dette skal være = data fra GPS so retunerer lat værdi
                gps_lng_variable = RunGPSLNG() # Dette skal være = data fra GPS so retunerer lng værdi
                
                json_data = {
                    "FALLEN": fallen_variable, 
                    "HEARTH_RATE": heart_variable,
                    "gpslat" :  gps_lat_variable,
                    "gpslng" :  gps_lng_variable   
                }

                print("Trying to send Json data")
                message = json.dumps(json_data)
                print(message)
                socket.send_string(message)
                time.sleep(5)
                
            elif imu_data == "imu_good":
                print("Everything is good")
                
                json_data1 = {
                    "STANDING":"YES" 
                }
                print("Trying to send Json data")
                message = json.dumps(json_data1)
                print(message)
                socket.send_string(message)
                time.sleep(5)
                
                
    except KeyboardInterrupt:
        socket.close()
        context.term()
        

send_rpi_data()