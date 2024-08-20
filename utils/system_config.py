import pyb
import time
import sensor
import gif

'''
Module to define what happens during:
1. Sleep mode (Timed and triggered)
2. Wake up from sleep mode
3. Set up real time clock
4. Motion sensor (AND logic for microwave and PIR sensor returns a boolean)
5. Record video (defaults to 10 seconds)/ take a picture
6. Transmit data to the cloud
'''
class SetupSystem:
    # turn led on and off green and blue
    def led_on(self, color=None):
        '''
        Function to turn on the LED
        This function will turn on the LED based on the color
        color: string value to indicate the color of the LED (green/blue)
        '''
        if color == "green":
            # if other color is on turn it off
            pyb.LED(3).off()
            pyb.LED(1).off()
            pyb.LED(2).on()
        elif color == "blue":
            # if other color is on turn it off
            pyb.LED(2).off()
            pyb.LED(1).off()
            pyb.LED(3).on()
        elif color is None:
            pyb.LED(1).off()
            pyb.LED(2).off()
            pyb.LED(3).off()
        else:
            raise ValueError("Invalid color")

    # Configuring the real time clock
    def set_rtc(self, set_time):
        '''
        Function to set the real time clock
        This function can be called only when system initial boot up
        This function will set the real time clock to the current time
        set_time: tuple of the current time (year, month, day, weekday, hour, minute, second, subsecond)
        '''
        # Set the RTC time
        rtc = pyb.RTC()
        # Set the RTC time to the current time
        return rtc.datetime(set_time) # (year, month, day, weekday, hour, minute, second, subsecond)

    # Check the current time returns a boolean if after 6pm
    def check_time(self):
        '''
        Function to check the current time
        This function will check the current time
        The function will return a boolean value to indicate if the current time is after 6pm
        '''
        current_time = time.localtime()
        hour = current_time[3]
        if hour >= 18:
            return True
        else:
            return False

    # Initialize the camera sensor
    def init_camera(self):
        '''
        Function to initialize the camera sensor
        This function will reset the camera sensor
        Set the pixel format to RGB565
        Set the frame size to HVGA (320x240)
        Skip the frames for the settings to take effect
        '''
        # Initialize the camera
        sensor.reset()
        sensor.set_pixformat(sensor.RGB565) # RGB format
        sensor.set_framesize(sensor.QVGA) # Set frame size to QVGA (320x240)
        sensor.skip_frames(time=2000)  # Let the camera adjust

    # Microwave motion sensor
    def microwave_sensor(self):
        '''
        Function to check the microwave sensor
        This function will check the microwave sensor
        The microwave sensor will be used to detect motion
        Returns a boolean value to indicate motion
        '''
        motion_sensor_pin = pyb.Pin('P8', pyb.Pin.IN)
        if motion_sensor_pin.value() == 1:
            return True
        else:
            return False

    # PIR motion sensor
    def pir_sensor(self):
        '''
        Function to check the PIR sensor
        This function will check the PIR sensor
        The PIR sensor will be used to detect motion
        Returns a boolean value to indicate motion
        '''
        pirSensor = pyb.Pin('P7', pyb.Pin.IN)#pyb.Pin.PULL_DOWN
        if pirSensor.value() == 1:
            return True
        else:
            return False

    # AND logic for microwave and PIR sensor
    def motion_sensed(self):
        '''
        Function to check the motion sensor
        This function will check the motion sensor (Microwave and PIR)
        The PIR is set to listen to the interrupt pin
        The microwave sensor is set to confirm the PIR sensor output (AND logic)
        Returns a boolean value to indicate motion 
        '''
        if self.microwave_sensor() and self.pir_sensor():
            return True
        else:
            return False

    # Record video
    def record_video(self, duration=10, frame_rate=30):
        '''
        Function to record video
        This function will record a video
        The video will be stored in the SD card
        The default duration of the video is 10 seconds
        '''
        # turn on blue led to indicate recording
        self.led_on("blue")
        # Get the current time
        current_time = time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".gif"
        print("Current Time: ", current_time)

        # FPS clock
        clock = time.clock()

        # Create a GIF object with the file name based on the current time
        directory = "/vids/"
        file_path = directory + current_time
        try:
            g = gif.Gif(file_path, loop=True)
            print("GIF file created: ", file_path)
        except Exception as e:
            print("Failed to create GIF file: ", e)
            raise

        # Based on the duration and the frame rate, calculate the number of frames
        num_frames = duration * frame_rate
        try:
            for i in range(num_frames):
                clock.tick()
                g.add_frame(sensor.snapshot(), delay=int(clock.avg() / 10))  # Delay in centiseconds
        except Exception as e:
            print("Failed to add frame: ", e)
        finally:
            # Close the GIF file
            g.close()

    # Configuring MCU for sleep mode
    def sleep_mode(self, timer=None, trigger=None):
        '''
        Function to put the camera in sleep mode
        This function can be triggered by a timer or event based trigger
        Timed trigger indicates the time to sleep till the following day
        trigger indicates the event to put the camera to sleep till an event occurs
            - Shutdown the camera sensor
            - Put the board to sleep
        '''
        # Put the camera to sleep for a timed duration 
        if timer:
            # Put the camera to sleep for the timed duration (12 hours)
            sensor.sleep(True)
            time.sleep(43200)  # Sleep for 12 hours
        elif trigger:
            # Put the camera to sleep until an event occurs
            sensor.sleep(True)
            # Put the board to sleep
            # pyb.stop()
        
    # Configuring MCU for wake up mode
    def wake_up(self):
        '''
        Function to wake up the camera from sleep mode
        This function can be triggered by a timer or an interrupt
        Timed trigger indicates the time to wake up from deep sleep (overnight)
        Interrupt trigger indicates the event to wake up the camera after an event occurs
            - Reset the camera sensor
            - Set the configurations for the camera sensor
        '''
        # Wake up the camera from sleep mode
        try:
            sensor.sleep(False)
        except Exception as e:
            print("Failed to wake up the camera: ", e)
            
        # Initialize the camera sensor
        # init_camera()

    # Configuring the data capture
    def data_capture(self):
        '''
        Function to capture data
        This function will capture data from the camera sensor
        The data can be a video or a picture (default is a video but defined in the argument)
        The data will be stored in the SD card
        '''
        pass

    # Configuring the data transmission
    def transmit_data(self):
        '''
        Function to transmit data
        This function will transmit data to the cloud
        The data can be a video or a picture (default is a video but defined in the argument)
        The data will be transmitted to the cloud
        Data transmission will be done using the MQTT protocol/HTTP protocol/FTP protocol/SMTP protocol/
        UDP protocol/TCP protocol/LoRa protocol/Sigfox protocol/NB-IoT protocol/Bluetooth protocol/
        Zigbee protocol/RF protocol/IR protocol
        '''
        pass