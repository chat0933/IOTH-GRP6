import zmq
import time
#import gps


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")


try:
    #for times in range(2):
    test_number = 0
    while True:
        if test_number == 0:
            message = f"Danger"#{times}"  #Beskeden her skal afgøres af enten IMU eller EKG
            print(f"Sending: {message}")
            socket.send_string(message)
            time.sleep(5)
            test_number = test_number+1
        
        elif test_number == 1:
            message = f"Dange"#{times}"  #Beskeden her skal afgøres af enten IMU eller EKG
            print(f"Sending: {message}")
            socket.send_string(message)
            time.sleep(5) 
            test_number = test_number -1

except KeyboardInterrupt:
    socket.close()
    context.term()
    #socket.disconnect()
    #socket.send_string("Hello, ZeroMQ!")