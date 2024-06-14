import pyb


'''
Module to define what happens during:
1. Sleep mode (Timed and triggered)
2. Wake up from sleep mode
3. Set up real time clock
4. Motion sensor (AND logic for microwave and PIR sensor returns a boolean)
5. Record video (defaults to 10 seconds)/ take a picture
6. Transmit data to the cloud
'''


# Configuring MCU for sleep mode
def sleep_mode():
    '''
    Function to put the camera in sleep mode
    This function can be triggered by a timer or event based trigger
    Timed trigger indicates the time to sleep till the following day
    trigger indicates the event to put the camera to sleep till an event occurs
        - Shutdown the camera sensor
        - Put the board to sleep

    '''
    pass

# Configuring MCU for wake up mode
def wake_up():
    '''
    Function to wake up the camera from sleep mode
    This function can be triggered by a timer or an interrupt
    Timed trigger indicates the time to wake up from deep sleep (overnight)
    Interrupt trigger indicates the event to wake up the camera after an event occurs
        - Reset the camera sensor
        - Set the configurations for the camera sensor
    '''
    pass

# Configuring the real time clock
def set_rtc(set_time):
    '''
    Function to set the real time clock
    This function can be called only when system initial boot up
    This function will set the real time clock to the current time
    set_time: tuple of the current time (year, month, day, weekday, hour, minute, second, subsecond)
    '''
    # Set the RTC time
    rtc = pyb.RTC()
    # Set the RTC time to the current time
    return rtc.datetime() # (year, month, day, weekday, hour, minute, second, subsecond)



# Configuring the motion sensor
def motion_sensor():
    '''
    Function to check the motion sensor
    This function will check the motion sensor (Microwave and PIR)
    The PIR is set to listen to the interrupt pin
    The microwave sensor is set to confirm the PIR sensor output (AND logic)
    Returns a boolean value to indicate motion 
    '''
    pass

# Configuring the data capture
def data_capture():
    '''
    Function to capture data
    This function will capture data from the camera sensor
    The data can be a video or a picture (default is a video but defined in the argument)
    The data will be stored in the SD card
    '''
    pass

# Configuring the data transmission
def transmit_data():
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
