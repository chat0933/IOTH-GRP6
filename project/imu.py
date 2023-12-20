import smbus
import time
import led

# I2C bus (use 1 for Raspberry Pi)
bus = smbus.SMBus(1)

# MPU-6050 address
mpu_address = 0x68  # You may need to adjust this based on your MPU-6050 address

# Wake up the MPU-6050 and configure as needed
bus.write_byte_data(mpu_address, 0x6B, 0)

def read_word(reg):
    high = bus.read_byte_data(mpu_address, reg)
    low = bus.read_byte_data(mpu_address, reg + 1)
    value = (high << 8) + low
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val

def run_imu():
    while True:
        try:
            # Read accelerometer data
            accel_x = read_word_2c(0x3B)
            accel_y = read_word_2c(0x3D)
            accel_z = read_word_2c(0x3F)

            # Read gyroscope data
            gyro_x = read_word_2c(0x43)
            gyro_y = read_word_2c(0x45)
            gyro_z = read_word_2c(0x47)

            print(f"Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")
            print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

            
            #Dette bruges til at teste og finde ud af hvad de rigtige tal ville være 
            if accel_x < -200:
                return "True"
            else:
                print("Nothing is wrong")
            

            # Der skal nok være noget return her
            time.sleep(1)
        except KeyboardInterrupt:
            print("Turning off LED and GPS")
            led.turn_off()
