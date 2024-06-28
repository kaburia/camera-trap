import sensor, time ,pyb

# Setup the camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

pir_pin = pyb.Pin('P7', pyb.Pin.IN, pyb.Pin.PULL_DOWN)

#mw_pin = pyb.Pin('P0', pyb.Pin.IN)

recording = False
video = None
record_time = 10

sensor.sleep(True)

def check_motion(pir_pin):
    # Read the state of the sensors
    pir_state = pir_pin.value()
    #mw_state = mw_pin.value()

    # Return True if both sensors are triggered, False otherwise
    return pir_state == 1 #and mw_state == 1



while(True):

    # Check if motion is detected
    # Replace this with your actual motion detection code
    motion_detected = check_motion(pir_pin)

    if motion_detected:
        # Wake up the camera if it's in sleep mode
       sensor.sleep(False)

       print("Motion detected!")
       # Capture an image
       img = sensor.snapshot()
       # Save the image
       img.save("/motion/motion_detected.jpg")

       sensor.sleep(True)
       print("slept")


    else:
        print("No motion.")

        time.sleep(2)
