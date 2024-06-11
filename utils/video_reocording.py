# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Face Detection Example
#
# This example shows off the built-in face detection feature of the OpenMV Cam.
#
# Face detection works by using the Haar Cascade feature detector on an image. A
# Haar Cascade is a series of simple area contrasts checks. For the built-in
# frontalface detector there are 25 stages of checks with each stage having
# hundreds of checks a piece. Haar Cascades run fast because later stages are
# only evaluated if previous stages pass. Additionally, your OpenMV Cam uses
# a data structure called the integral image to quickly execute each area
# contrast check in constant time (the reason for feature detection being
# grayscale only is because of the space requirement for the integral image).

import sensor
import time
import image
import gif
import machine
import os

# Reset sensor
sensor.reset()

# Initialize the sensor and set configurations
sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.HVGA)  # Set frame size to QVGA (320x240)
sensor.skip_frames(time=2000)  # Wait for settings to take effect.

# Initialize the red LED
led = machine.LED("LED_RED")

led.on()

# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
face_cascade = image.HaarCascade("frontalface", stages=25)
print(face_cascade)

# FPS clock
clock = time.clock()

while True:
    clock.tick()

    # Capture snapshot
    img = sensor.snapshot()

    # Find objects.
    # Note: Lower scale factor scales-down the image more and detects smaller objects.
    # Higher threshold results in a higher detection rate, with more false positives.
    objects = img.find_features(face_cascade, threshold=0.85, scale_factor=1.25)

    # 

    # # Draw objects
    # for r in objects:
    #     img.draw_rectangle(r)

    # Start recording the GIF if a face is detected
    if len(objects) > 0:
        # Get the current date and time
        current_time = time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".gif"
        print("Current Time: ", current_time)

        # Ensure the directory exists
        directory = "/vids_face/"
#        if not os.path.exists(directory):
#            os.mkdir(directory)

        # Create a GIF object with the file name based on the current time
        file_path = directory + current_time
        try:
            g = gif.Gif(file_path, loop=True)
            print("GIF file created: ", file_path)
        except Exception as e:
            print("Failed to create GIF file: ", e)
            led.off()
            raise

        # Record 100 frames and add them to the GIF
        try:
            for i in range(100):
                clock.tick()
                g.add_frame(sensor.snapshot(), delay=int(clock.avg() / 10))  # Delay in centiseconds
                # print(clock.fps())
        except Exception as e:
            print("Failed to add frame: ", e)
        finally:
            # Close the GIF file
            g.close()

        # Turn off the LED
        led.off()
    led.on()

    # Print FPS.
    # Note: Actual FPS is higher, streaming the FB makes it slower.
    print(clock.fps())
