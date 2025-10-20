import board
import digitalio
import analogio
import touchio
import busio
import time
import adafruit_mpr121
from adafruit_mpu6050 import MPU6050
import math

print("Still going boss")

#setting up i2c sensors (MPR121, MPU6050)
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)
touch_pad = adafruit_mpr121.MPR121(i2c)
tilt_sensor = MPU6050(i2c)

#initialize GP14 as tilt, circuit closed when flat 
tilt_switch = digitalio.DigitalInOut(board.GP14)
tilt_switch.direction = digitalio.Direction.INPUT

#track for capacative sensor, starts as false and is set within function
last_touched = [False] * 12

#track for tilt sensor
last_state_tilt = False

#setup LED
touch_led = digitalio.DigitalInOut(board.GP16)
touch_led.direction = digitalio.Direction.OUTPUT

tilt_led = digitalio.DigitalInOut(board.GP17)
tilt_led.direction = digitalio.Direction.OUTPUT

def touched():
    for i in range(12):
        currently_touched = touch_pad[i].value
        
        #prints out which pin is touched once, then prints once when released
        if currently_touched and not last_touched[i]:
            print(f"Pad {i} touched")
        elif not currently_touched and last_touched[i]:
            print(f"Pad {i} released")

        last_touched[i] = currently_touched

def ledOn():
    touch_led.value = touch_pad[11].value
    tilt_led.value = not tilt_switch.value
    

def tilt():
    global last_state_tilt
    current_state = not tilt_switch.value
    
    #only trigger on state change
    if current_state != last_state_tilt:
        time.sleep(0.05) #debounce
        if current_state == (not tilt_switch.value):
            last_state_tilt = current_state
            if current_state:
                print("Tilted!")
                tilt_led.value = True
            else:
                print("Flat")
                tilt_led.value = False
                
def tilt_sense():
    xAccel = round(tilt_sensor.acceleration[0], 1)
    yAccel = round(tilt_sensor.acceleration[1], 1)
    zAccel = round(tilt_sensor.acceleration[2], 1)
    
    #the math to get the degrees of tilt
    mag = math.sqrt(xAccel**2 + yAccel**2 + zAccel**2)
    zNormalized = zAccel / mag
    
    theta = math.acos(zNormalized) #only takes values between -1 and 1, so had to do that other stuff to compensate for gravity
    thetaDeg = math.degrees(theta)
    
    
    #print(f"x: {xAccel} m/s^2, y: {yAccel} m/s^2, z: {zAccel} m/s^2")
    print("Tilt angle: ", thetaDeg)

while True:
    touched()
    #tilt()
    tilt_sense()
    ledOn()
    time.sleep(0.5)
