import sensor, image, pyb,time

# Initialize the camera sensor.
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.VGA)
sensor.skip_frames(time = 2000)

# Use one of the digital pins for the motion sensor (e.g., 'P6').
motion_sensor_pin = pyb.Pin('P8', pyb.Pin.IN)

while(True):
    # Check if the motion sensor pin is high (motion detected).
    if motion_sensor_pin.value() == 1:
        print("Motion detected! Taking picture...")
        img = sensor.snapshot()
        img.save("motion-capture.jpg")
        # Add a delay to avoid multiple captures for one motion event

    else:print("no motion")

    time.sleep(2)
# Code for Microwave Sensor to detect motion
