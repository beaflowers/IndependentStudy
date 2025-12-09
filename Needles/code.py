import board
import digitalio
import analogio
import time

#initialize GP14 as tilt, circuit closed when flat 
tilt_switch = digitalio.DigitalInOut(board.GP14)
tilt_switch.direction = digitalio.Direction.INPUT

#track for tilt sensor
last_state_tilt = False

#configure analog input pins (photoresistor)
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

def photo_sense():
    global light_threshold, light_baseline
    light_test = light_baseline + light_threshold #changes if it gets darker
    if light.value > light_test:
        light_led.value = True
        print("Light triggered")
    else:
        light_led.value = False
        
def read_touch():
    if touch.value == False: #means it is touched -> pulled to ground
        print("Touched")
        touch_led.value = True;
    else:
        touch_led.value = False;
    
while True:
    tilt()
    photo_sense()
    read_touch()
    
    time.sleep(0.5)
