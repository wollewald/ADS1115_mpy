########################################################################################
#     Example program for the ADS1115_mPy module
#
#     This program shows how to use two ADS1115 modules. In order to set the address, 
#     connect the address pin to:
#      
#     GND -> 0x48 (or leave unconnected)
#     VCC -> 0x49
#     SDA -> 0x4A
#     SCL -> 0x4B
#      
#     When you have understood how it works you can easily add two additional ADS1115.
#     Of course there is potential to shorten the code, e.g. by setting up the ADCs 
#     as array.
#      
#     If you need up to eight ADS1115 modules you can use an ESP32 with its two I2C 
#     interfaces.
# 
#     If you need up to 32 ADS1115 modules you can use a multiplexer like the TSCA9548A.
#       
#     Or you combine both and control up to 64 ADS1115 modules.
#       
# Further information can be found on (currently only for the Arduino version):
# https://wolles-elektronikkiste.de/ads1115 (German)
# https://wolles-elektronikkiste.de/en/ads1115-a-d-converter-with-amplifier (English)
#
########################################################################################

from machine import I2C, Pin
from time import sleep
from ADS1115 import *

I2C_ADDRESS_1 = 0x48
I2C_ADDRESS_2 = 0x49

i2c = I2C(0)
adc_1 = ADS1115(I2C_ADDRESS_1, i2c=i2c)
adc_2 = ADS1115(I2C_ADDRESS_2, i2c=i2c)

adc_1.setVoltageRange_mV(ADS1115_RANGE_6144)
adc_1.setMeasureMode(ADS1115_CONTINUOUS) 
adc_1.setCompareChannels(ADS1115_COMP_0_GND)
  
adc_2.setVoltageRange_mV(ADS1115_RANGE_6144)
adc_2.setMeasureMode(ADS1115_CONTINUOUS) 
adc_2.setCompareChannels(ADS1115_COMP_0_GND)

while True:
    voltage = adc_1.getResult_V()
    print("Voltage [V], ADS1115 No 1: {:<4.2f}".format(voltage))
    voltage = adc_2.getResult_V()
    print("Voltage [V], ADS1115 No 1: {:<4.2f}".format(voltage))
 
    print("****************************")  
    sleep(1)
