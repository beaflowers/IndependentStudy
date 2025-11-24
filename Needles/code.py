import board
import digitalio
import analogio
import touchio
import busio
import time
import adafruit_mpr121
from adafruit_mpu6050 import MPU6050
import math

#setting up i2c bus - possibly no longer needed
#setting up i2c sensors (MPR121, MPU6050)
#i2c = busio.I2C(scl=board.GP7, sda=board.GP6)
#touch_pad = adafruit_mpr121.MPR121(i2c)
#tilt_sensor = MPU6050(i2c)

#initialize GP14 as tilt, circuit closed when flat 
tilt_switch = digitalio.DigitalInOut(board.GP14)
tilt_switch.direction = digitalio.Direction.INPUT

#track for tilt sensor
last_state_tilt = False

#configure analog input pins
light = analogio.AnalogIn(board.GP27)

#setup for photoresistor
light_baseline = light.value
light_threshold = 3000

#setup for wire touch
touch = digitalio.DigitalInOut(board.GP21)
touch.direction = digitalio.Direction.INPUT
touch.pull = digitalio.Pull.UP #wont short circuit

#setup LED

tilt_led = digitalio.DigitalInOut(board.GP17)
tilt_led.direction = digitalio.Direction.OUTPUT

light_led = digitalio.DigitalInOut(board.GP19)
light_led.direction = digitalio.Direction.OUTPUT

touch_led = digitalio.DigitalInOut(board.GP20)
touch_led.direction = digitalio.Direction.OUTPUT


    
def tilt():
    global last_state_tilt
    current_state = not tilt_switch.value

    # only trigger on state change
    if current_state != last_state_tilt:
        time.sleep(0.05)  # debounce

        # verify the state is still the same after debounce
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

def photo_sense():
    global light_threshold, light_baseline
    light_test = light_baseline + light_threshold #changes if it gets darker
    if light.value > light_test:
        light_led.value = True
    else:
        light_led.value = False
        
    print(f"Light level: {light.value}")
    
def read_touch():
    if touch.value == False: #means it is touched -> pulled to ground
        print("Touched")
        touch_led.value = True;
    else:
        touch_led.value = False;
    
while True:
    tilt()
    #tilt_sense()
    #photo_sense()
    #motion()
    read_touch()
    
    time.sleep(0.5)
