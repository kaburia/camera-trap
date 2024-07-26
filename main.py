"""
 Copyright 2024 Dedan Kimathi University of Technology
 Author: Austin Kaburia (Github: @kaburia)
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from utils.system_config import SetupSystem
settings = SetupSystem()

# set up the system
# Set up the real time clock
settings.set_rtc((2024, 7, 25, 18, 10, 0, 0, 0))

# Initialize the camera sensor
settings.init_camera()

# Infinite loop to check for motion
while True:
    # Check if motion is detected
    if settings.motion_sensed():
        # Wake up the camera
        settings.wake_up()
        # Check time
        if settings.check_time(): # after 6pm
            # Transmit the Data
            
            # Sleep the system till the next day (for 12 hours)
            # settings.sleep_mode(timer=True)
            pass
        else: # before 6pm
            # record the video
            settings.record_video()
    else:
        # trigger sleep mode
        settings.sleep_mode(trigger=True)
