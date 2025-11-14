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

#GP13 as motion sensor
motion_sense = digitalio.DigitalInOut(board.GP13)
motion_sense.direction = digitalio.Direction.INPUT

#track for capacative sensor, starts as false and is set within function
last_touched = [False] * 12

#track for tilt sensor
last_state_tilt = False

#track for temp sensor
temp_change = False
temp_time = 0

#configure analog input pins
therm = analogio.AnalogIn(board.GP28)
light = analogio.AnalogIn(board.GP27)

# circuit values - basic stuff to make theristor work?
SERIES_RESISTOR = 10000     # 10k resistor on board
BETA = 3950                 # Common thermistor beta value - describes how resistance changes with temperature
NOMINAL_RESISTANCE = 10000  # Thermistor resistance at 25°C
NOMINAL_TEMP = 25           # 25°C baseline

def calibrate(samples=10, delay=0.1):
    total = 0
    for _ in range(samples):
        total+= therm_sense()
        time.sleep(delay)
    return total / samples

def therm_sense():
     # Convert analog pin reading to voltage (0–65535 range)
    voltage = therm.value * 3.3 / 65535
    #print("ADC voltage:", voltage)
    
    # Convert voltage to resistance in a voltage divider
    resistance = SERIES_RESISTOR * ((3.3 / voltage) - 1)
    #print("Calculated resistance:", resistance)

    # Beta formula to convert resistance to temperature
    #this is some math i looked up. it measures in kelvins and we have to convert to C
    #it's called steinhart bc that's the name of the forumla 
    steinhart = math.log(resistance / NOMINAL_RESISTANCE) #tells how far the resistance has shifted from nominal
    steinhart /= BETA #adjusts for thermistor sensitivity
    steinhart += 1.0 / (NOMINAL_TEMP + 273.15) #offsets to the nominal temperature
    steinhart = 1.0 / steinhart #takes the reciprocal, solves for T in Kelvin
    temp_c = steinhart - 273.15 #converts to celsius
    
    return temp_c

#calibrating thermistor
print("Calibrating room temp...")
baseline = calibrate()
print(f"Room baseline: {baseline:.2f}°C")
last_temp = baseline
threshold = 1.0

#setup for photoresistor
light_baseline = light.value
light_threshold = 3000

#setup LED
touch_led = digitalio.DigitalInOut(board.GP16)
touch_led.direction = digitalio.Direction.OUTPUT

tilt_led = digitalio.DigitalInOut(board.GP17)
tilt_led.direction = digitalio.Direction.OUTPUT

temp_led = digitalio.DigitalInOut(board.GP18)
temp_led.direction = digitalio.Direction.OUTPUT

light_led = digitalio.DigitalInOut(board.GP19)
light_led.direction = digitalio.Direction.OUTPUT

mo_led = digitalio.DigitalInOut(board.GP20)
mo_led.direction = digitalio.Direction.OUTPUT

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
    #touch_led.value = touch_pad[11].value
    #tilt_led.value = not tilt_switch.value
    temp_led.value = temp_change
    mo_led.value = motion_sense.value
    
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


def use_therm():
    global baseline, temp_change, temp_time
    temp = therm_sense()
    threshold = 2
    
    #detect change in temp and trigger if not already changed
    if not temp_change and abs(temp - baseline) > threshold:
        temp_change = True;
        temp_time = time.monotonic() #record time
        print(temp_change)
        
    #reset after 2 seconds
    if temp_change and time.monotonic() - temp_time > 2:
        temp_change = False;
       
    print(f"Temp: {temp:.2f}°C")
 
def motion():
    if motion_sense.value:
        print("Movement Detected")

def photo_sense():
    global light_threshold, light_baseline
    light_test = light_baseline + light_threshold #changes if it gets darker
    if light.value > light_test:
        light_led.value = True
    else:
        light_led.value = False
        
    print(f"Light level: {light.value}")
    print(f"Light test: {light_test}")
    
while True:
    #touched()
    #tilt()
    #tilt_sense()
    use_therm()
    photo_sense()
    motion()
    
    ledOn()
    time.sleep(0.5)
