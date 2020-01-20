from dronekit import *
import time

vehicle = connect('udp:127.0.0.1:14550',wait_ready=True,baud=57600)

def arm_and_takeoff(aTargetAltitude):

    print("Basic pre-arm checks")
    
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


arm_and_takeoff(10)

vehicle.mode = VehicleMode("RTL")

vehicle.close()
