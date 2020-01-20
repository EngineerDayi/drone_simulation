#Plug your telemtry module and run this script

from dronekit import *
import time 

vehicle = connect('/dev/ttyUSB0',wait_ready=False,baud=57600)


while True:

    print("Mode : ",vehicle.mode.name)
    print("Is armable? : ",vehicle.is_armable)
    time.sleep(1)
