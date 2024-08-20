import sensor, image, time
from pyb import Pin, SPI
from nrf24l01 import NRF24L01

# Initialize the camera
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# Initialize SPI
spi = SPI(2, SPI.MASTER, baudrate=10000000, polarity=0, phase=0)
csn = Pin('P3', Pin.OUT_PP, value=1)
ce = Pin('P4', Pin.OUT_PP, value=0)

# Initialize the NRF24L01 module
nrf = NRF24L01(spi, csn, ce, channel=100, payload_size=32)
print('any')
# Set the address
nrf.open_rx_pipe(1, b'\xd2\xf0\xf0\xf0\xf0')
nrf.start_listening()

# Function to receive data
def receive_data():
    while True:
        if nrf.any():
            payload = nrf.recv()
            print("Received:", payload)
            # Process the received data as needed
        time.sleep(0.1)

# Main loop
try:
    receive_data()
except KeyboardInterrupt:
    print("Program interrupted")
