# Code for the PIR sensor to detect motion
import sensor
import pyb
import time

# Initialize the PIR sensor pin
pir_sensor = pyb.Pin('P7', pyb.Pin.IN, pyb.Pin.PULL_DOWN)

# Initialize the camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)  # Let the camera adjust

# Main loop
while True:
    # Check the state of the PIR sensor
    if pir_sensor.value() == 1:
        print("Motion detected!")
        # Capture an image
        img = sensor.snapshot()
        # Save the image
        img.save("/motion/motion_detected.jpg")
        # Optional: Add a delay to avoid multiple triggers
#        time.sleep(500)  # Delay in milliseconds
    else:
        print("No motion.")
    
    # Sleep for a short time to reduce CPU usage
    time.sleep(0.1)
