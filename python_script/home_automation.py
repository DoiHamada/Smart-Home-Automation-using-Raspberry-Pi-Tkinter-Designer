import RPi.GPIO as GPIO
import time

relays = {"1":17,"2":27,"3":22,"4":23}


GPIO.setmode(GPIO.BCM)
for pin in relays.values():
    GPIO.setup(pin, GPIO.OUT)

def control_relay(command):
    parts = command.split()
    if len(parts) != 2:
        print("Invalid command!")
        return
    appliance, state = parts
    pin = relays.get(appliance)
    match state:
        case "ON" if pin:
            GPIO.output(pin, GPIO.LOW) # Turn ON
            print(f"Appliance {appliance} is now ON.")
        case "OFF" if pin:
            GPIO.output(pin, GPIO.HIGH) # Turn OFF
            print(f"Appliance {appliance} is now OFF.")
        case _:
            print("Invalid command!")    

try:
    while True:
        cmd = input("Enter command (e.g., '1 ON', '3 OFF' or 'EXIT' to stop. ").strip().upper()
        if cmd == "EXIT":
            print("Exit the Program!")
            for pin in relays.values():
                GPIO.output(pin, GPIO.HIGH) # Turn OFF
            GPIO.cleanup()
            break
        control_relay(cmd)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Stopped.")

