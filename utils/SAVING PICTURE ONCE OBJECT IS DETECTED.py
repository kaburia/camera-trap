# Untitled - By: waith - Fri Apr 26 2024

#import sensor, image, time

#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)

#clock = time.clock()

#while(True):
 #   clock.tick()
  #  img = sensor.snapshot()
   # print(clock.fps())

import sensor, time, pyb
import random
import machine
import mjpeg
import os
from pyb import Pin

# Initialize the camera sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_exposure(False, exposure_us=150)
sensor.set_windowing((240, 240))
sensor.skip_frames(time = 5000)  # Wait for settings to take effect
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
#clock = time.clock()
# Microwave sensor setup
microwave_pin = Pin('P0', Pin.IN)  # Change 'P7' to your connected pin

led = machine.LED("LED_RED")

if not "temp" in os.listdir():
    os.mkdir("temp")  # Make a temp directory

while True:
  if microwave_pin.value() == 1:
    # Object detected, capture image
    #clock.tick()
    img = sensor.snapshot()
    sensor.snapshot().save("temp/bg.bmp")
    print("Image captured")
  else:
    print("No Image captured")

  time.sleep(2000)

# Initialize LEDs for indication
#red_LED = pyb.LED(1)
#green_LED = pyb.LED(2)
#blue_LED = pyb.LED(3)

#def setLED(color):
   # """Control LEDs based on specified color"""
 #   red_LED.off()
  #  green_LED.off()
   # blue_LED.off()
    #if color == 'red':
     #   red_LED.on()
    #elif color == 'green':
     #   green_LED.on()
    #elif color == 'blue':
     #   blue_LED.on()

#while True:
    # Check microwave sensor
 #   if microwave_pin.value() == 1:
        # Object detected, capture image
  #      img = sensor.snapshot()
   #     print("Image captured")
    #    setLED('green')  # Green LED indicates capture

        # Process the image or do further actions here
        # For demonstration, just toggle LED colors
       #setLED('red')  # Red LED indicates processing

        # Optionally, add image processing code here

        #setLED('blue')  # Blue LED indicates process complete
 #  else:
        # No object detected, no action required
  #      setLED('none')  # Turn off LEDs

   # time.sleep(1000)  # Check every 1000 milliseconds
