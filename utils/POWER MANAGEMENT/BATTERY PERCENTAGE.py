# Untitled - By: waith - Tue Jun 25 2024

import sensor, image, time
from pyb import ADC, Pin
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)



# ADC pin where the battery voltage is connected
adc_pin = 'P6'  # Change this to the appropriate ADC pin number

# Create ADC object on the specified pin
adc = ADC(Pin(adc_pin))

# Configure ADC (this varies by board)
# e.g., on ESP32 you might need to set the attenuation
# adc.atten(ADC.ATTN_11DB)  # Configure the attenuation (0dB, 2.5dB, 6dB, or 11dB)

# Reference values for battery voltage (adjust these based on your battery)
V_MAX = 3.2  # Maximum voltage of a fully charged battery
V_MIN = 2.0  # Minimum voltage of a discharged battery

def read_battery_voltage():
    # Read the raw ADC value
    adc_value = adc.read()

    # Convert ADC value to voltage
    # Assuming the ADC range is 0-4095 and reference voltage is 3.3V
    voltage = adc_value / 4095.0 * 3.3

    # If using a voltage divider, multiply by the appropriate factor
    # voltage = voltage * (R1 + R2) / R2

    return voltage

def voltage_to_percentage(voltage):
    # Clamp the voltage to be within V_MIN and V_MAX
    voltage = max(V_MIN, min(voltage, V_MAX))

    # Calculate the battery percentage
    percentage = (voltage - V_MIN) / (V_MAX - V_MIN) * 100

    return percentage

while True:
    # Read the battery voltage
    voltage = read_battery_voltage()

    # Convert voltage to percentage
    percentage = voltage_to_percentage(voltage)

    # Print the battery voltage and percentage
    print("Battery Voltage: {:.2f}V, Battery Percentage: {:.2f}%".format(voltage, percentage))

    # Wait for a while before the next reading
    time.sleep(10)

