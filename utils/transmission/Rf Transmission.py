# Untitled - By: waith - Tue Jun 25 2024

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

import time
from machine import Pin, SPI
from nrf24l01 import NRF24L01

# Initialize SPI
spi = SPI(2, baudrate=10000000, polarity=0, phase=0)
csn = Pin('P3', mode=Pin.OUT, value=1)
ce = Pin('P4', mode=Pin.OUT, value=0)

# Initialize the NRF24L01 module
nrf = NRF24L01(spi, csn, ce, channel=100, payload_size=32)

# Set the address
nrf.open_tx_pipe(b'\xe1\xf0\xf0\xf0\xf0')
nrf.open_rx_pipe(1, b'\xd2\xf0\xf0\xf0\xf0')

# Read binary file
#def read_binary_file(file_path):
    #with open(file_path, 'rb') as f:
def read_binary_file_in_chunks(file_path, chunk_size=32):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Reference the file in the 'data' subdirectory
file_path = '/data/example.bin'

# Read the binary file from the specified directory
try:
    for chunk in read_binary_file_in_chunks(file_path, chunk_size=32):
        # Send each chunk via NRF24L01
        nrf.send(chunk)
        ce.value(1)  # Set CE high to start transmission
        time.sleep(0.01)  # Maintain CE high for a short duration to transmit
        ce.value(0)  # Set CE low to go back to standby
        time.sleep(0.1)  # Short delay between transmissions
except OSError as e:
    print("Error reading file:", e)
        #return f.read()

#binary_data = read_binary_file('/example.bin')
#try:
   # binary_data = read_binary_file('/example.bin')
#except OSError as e:
    #print("Error reading file:", e)
    #binary_data = b''

# Send binary data in chunks
#chunk_size = 32
#for i in range(0, len(binary_data), chunk_size):
    #chunk = binary_data[i:i+chunk_size]
    #nrf.send(chunk)
    #time.sleep(0.1)  # Short delay between transmissions
    #ce.value(1)  # Set CE high to start transmission
    #time.sleep(0.01)  # Maintain CE high for a short duration to transmit
    #ce.value(0)  # Set CE low to go back to standby
    #time.sleep(0.1)  # Short delay between transmissions
