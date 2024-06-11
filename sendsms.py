# Untitled - By: LENOVO - Wed May 29 2024

import serial
import time

# Open serial port
ser = serial.Serial('P6', 9600, timeout=5)

# Function to send an SMS
def send_sms(phone_number, message):
    ser.write(b'AT+CMGF=1\r')  # Set GSM to text mode
    time.sleep(2)
    command = f'AT+CMGS="{phone_number}"\r'
    ser.write(command.encode())  # Set recipient number
    time.sleep(2)
    ser.write((message + '\x1A').encode())  # Send message and a ctrl+z end character

# Use the function
send_sms("+25435565139", "Hello, this is a test message!")

# Close the serial port
ser.close()
