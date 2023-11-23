import ekg_ecg
import neopixel
import board
import smbus
import time

bus = smbus.SMBus(1) # RPI revision 2 (0 for evision 1)
i2c_address = 0x49 #default address

# Initialize NeoPixel LED ring
pixel_pin = board.D10
num_pixels = 12
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True, pixel_order=ORDER)

#ekg_value = 120

# THIS IS ONLY A TEST
def set_neopixel_leds(ekg_value):
    while True:
    # code to set NeoPixel LED color based on pH value through the ranges listed above
        try:
            if ekg_value <= 110:
                pixels.fill((255, 0, 0))
                #print("PH value is '0")
                
            elif ekg_value == 90-110:
                pixels.fill((0, 255, 0))
                #print("PH value is '1")
                #PH_VALUE = 1
            elif ekg_value >= 85:
                pixels.fill((255, 0, 0))
                #print("PH value is '2")

            time.sleep(1)
        except KeyboardInterrupt:
            pixels.fill((0,0,0))
            pixels.show()


                 #PH_VALUE = 2
            """
            elif ekg_value <= 80:
                pixels.fill((255, 255, 0))
                print("PH value is '3")
                PH_VALUE = 3
            """    
            """
            elif ANALOG_VALUE <= 160:
                pixels.fill((191, 255, 0))
                print("PH value is '4")
                PH_VALUE = 4
            elif ANALOG_VALUE <= 300:
                pixels.fill((128, 255, 0))
                print("PH value is '5")
                PH_VALUE = 5
            elif ANALOG_VALUE <= 450:
                pixels.fill((64, 255, 0))
                print("PH value is '6")
                PH_VALUE = 6
            elif ANALOG_VALUE <= 600:
                pixels.fill((0, 255, 0))
                print("PH value is '7")
                PH_VALUE = 7
            elif ANALOG_VALUE <= 650:
                pixels.fill((0, 255, 64))
                print("PH value is '8")
                PH_VALUE = 8
            elif ANALOG_VALUE<= 700:
                pixels.fill((0, 255, 128))
                print("PH value is '9")
                PH_VALUE = 9
            elif ANALOG_VALUE<= 750:
                pixels.fill((0, 255, 191))
                print("PH value is '10")
                PH_VALUE = 10
            elif ANALOG_VALUE <= 800:
                pixels.fill((0, 0, 255))
                print("PH value is '11")
                PH_VALUE = 11
            elif ANALOG_VALUE<= 900:
                pixels.fill((69, 0, 255))
                print("PH value is '12")
                PH_VALUE = 12
            elif ANALOG_VALUE <= 1000:
                pixels.fill((128, 0, 255))
                print("PH value is '13")
                PH_VALUE = 13
            elif ANALOG_VALUE <=1023:
                pixels.fill((197,0,255))
                print("PH value is 14")
                PH_VALUE = 14
            
            return PH_VALUE
            """