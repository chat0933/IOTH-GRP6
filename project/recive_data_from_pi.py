import zmq
import json
from led import set_colour_red,reset_colour,turn_off
import time
import sqlite3
import alarm_db as database

con = sqlite3.connect('patient_database.db')
cur = con.cursor()
database.create_user_table_chris()
database.create_issues_table_chris()

context = zmq.Context()

# Create a SUB socket
socket = context.socket(zmq.SUB)
socket.connect("tcp://your_ip_address:5555")
socket.subscribe(b"")


# Receive and print messages
def recieve_rpi_data():
    try:
        while True:
            message = socket.recv_string()
            message_data = json.loads(message)
            print(f"Received: {message}")

            if "FALLEN" in message: #Denne besked skal modtages fra imu
                print("SOMEONE HAS FALLEN IN BATTLE AND THEY CANT GET UP!")
                #time.sleep(2)
                
                fallen_value = message_data.get("FALLEN", "True") 
                heart_rate_value = (message_data.get("HEARTH_RATE", 0))
                gpslat_value = (message_data.get("gpslat",  0))
                gpslng_value = (message_data.get("gpslng", 0))
                
                print("Trying to insert data into databaes")
                cur.execute("INSERT INTO Issues(FALLEN, HEARTH_RATE, GPS1, GPS2) VALUES (?,?,?,?)",
                (fallen_value, heart_rate_value, gpslat_value, gpslng_value))

                con.commit()
                set_colour_red()
                

            else:
                reset_colour()
                #continue
                print("ALl good")
                time.sleep(5)
        
    except KeyboardInterrupt:
        # Close the socket and context on KeyboardInterrupt (Ctrl+C)
        socket.close()
        context.term()
        turn_off()
        con.close()
        print("Connection closed.")
    
recieve_rpi_data()
