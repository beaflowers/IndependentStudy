import board
import digitalio
import analogio
import touchio
import busio
import time
import adafruit_mpr121

print("Still going boss")

#MPR 121 for touch capacitive sensors
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)
touch_pad = adafruit_mpr121.MPR121(i2c)

#track for capacative sensor, starts as false and is set within function
last_touched = [False] * 12

#setup LED
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

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
    led.value = touch_pad[11].value 

while True:
    touched()
    ledOn()
    time.sleep(0.5)
