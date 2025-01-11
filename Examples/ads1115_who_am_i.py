####################################################################################
# Example sketch for the ADS1115_WE library
#
# This sketch checks whether you have an ADS1115 or ADS1015 module. The last 
# four bits of raw values obtained from an ADS1015 should be zero. Connect A0
# to a voltage different from GND. The sketch also checks how much time is 
# needed to perform ten measurements at lowest data rate, which is 128 SPS for
# the ADS1015 and 8 SPS for the ADS1115.
#  
# Further information can be found on:
# https://wolles-elektronikkiste.de/ads1115 (German)
# https://wolles-elektronikkiste.de/en/ads1115-a-d-converter-with-amplifier (English)
# 
####################################################################################

from machine import I2C, Pin
import time
from time import sleep
from ADS1115 import *

ADS1115_ADDRESS = 0x48

i2c = I2C(0)
adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)

adc.setVoltageRange_mV(ADS1115_RANGE_6144) 
adc.setCompareChannels(ADS1115_COMP_0_GND)
adc.setMeasureMode(ADS1115_SINGLE) 
print("ADS1115/ADS1015 Example Sketch - Who am I")
print("Performing 10 single ended conversions A0 vs. GND:");
print(" ");
#uint16_t checkSum = 0;

sum = 0
for i in range(10):
    adc.startSingleMeasurement()
    while adc.isBusy():
        pass
    raw = adc.getRawResult()
    print(bin(raw))
    sum = sum + raw%8

print("Check sum of last for bits", sum)


adc.setConvRate(ADS1115_8_SPS); # = ADS1015_128_SPS = 0x0000

startTime = time.ticks_ms()
for i in range(10):
    adc.startSingleMeasurement()
    while adc.isBusy():
        pass
duration = time.ticks_ms() - startTime
print("Time needed for 10 conversions at slowest sample rate [ms]: ", duration)

if (sum > 0) and (duration > 1000):
    print("I am an ADS1115!");
elif (sum == 0) and (duration < 1000):  
    print("I am an ADS1015!");
else:
    print("Sorry, I am not sure. Please run the program again!");

while True:
    sleep(1)