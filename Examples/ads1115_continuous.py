#####################################################################################
# Example program for the ADS1115_mPy module
#
# This program shows how to use the ADS1115 in continuous mode. 
#  
# Further information can be found on (currently only for the Arduino version):
# https://wolles-elektronikkiste.de/ads1115 (German)
# https://wolles-elektronikkiste.de/en/ads1115-a-d-converter-with-amplifier (English)
# 
#####################################################################################

from machine import I2C
from time import sleep
from ADS1115 import *

ADS1115_ADDRESS = 0x48

i2c = I2C(0)
adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)

#   ADS1115_RANGE_6144  ->  +/- 6144 mV
#   ADS1115_RANGE_4096  ->  +/- 4096 mV
#   ADS1115_RANGE_2048  ->  +/- 2048 mV (default)
#   ADS1115_RANGE_1024  ->  +/- 1024 mV
#   ADS1115_RANGE_0512  ->  +/- 512 mV
#   ADS1115_RANGE_0256  ->  +/- 256 mV
adc.setVoltageRange_mV(ADS1115_RANGE_6144)

#   ADS1115_COMP_0_1    ->  compares 0 with 1 (default)
#   ADS1115_COMP_0_3    ->  compares 0 with 3
#   ADS1115_COMP_1_3    ->  compares 1 with 3
#   ADS1115_COMP_2_3    ->  compares 2 with 3
#   ADS1115_COMP_0_GND  ->  compares 0 with GND
#   ADS1115_COMP_1_GND  ->  compares 1 with GND
#   ADS1115_COMP_2_GND  ->  compares 2 with GND
#   ADS1115_COMP_3_GND  ->  compares 3 with GND
#adc.setCompareChannels(ADS1115_COMP_0_GND)

#   ADS1115_ASSERT_AFTER_1  -> after 1 conversion
#   ADS1115_ASSERT_AFTER_2  -> after 2 conversions
#   ADS1115_ASSERT_AFTER_4  -> after 4 conversions
#   ADS1115_DISABLE_ALERT   -> disable comparator / alert pin (default) 
#adc.setAlertPinMode(ADS1115_ASSERT_AFTER_1)

#   ADS1115_8_SPS 
#   ADS1115_16_SPS  
#   ADS1115_32_SPS 
#   ADS1115_64_SPS  
#   ADS1115_128_SPS (default)
#   ADS1115_250_SPS 
#   ADS1115_475_SPS 
#   ADS1115_860_SPS 
adc.setConvRate(ADS1115_128_SPS)

#   ADS1115_CONTINUOUS  ->  continuous mode
#   ADS1115_SINGLE     ->  single shot mode (default)
adc.setMeasureMode(ADS1115_CONTINUOUS) 

#   Choose maximum limit or maximum and minimum alert limit (window) in Volt - alert pin will 
#   assert when measured values are beyond the maximum limit or outside the window
#   Upper limit first: setAlertLimit_V(MODE, maximum, minimum)
#   In max limit mode the minimum value is the limit where the alert pin assertion will be  
#   cleared (if not latched)  
# 
#   ADS1115_MAX_LIMIT
#   ADS1115_WINDOW
#adc.setAlertModeAndLimit_V(ADS1115_MAX_LIMIT, 3.0, 1.5)
  
#   Enable or disable latch. If latch is enabled the alert pin will assert until the
#   conversion register is read (getResult functions). If disabled the alert pin assertion will be
#   cleared with next value within limits. 
#   
#   ADS1115_LATCH_DISABLED (default)
#   ADS1115_LATCH_ENABLED
#adc.setAlertLatch(ADS1115_LATCH_ENABLED)

#   Sets the alert pin polarity if active:
# 
#   ADS1115_ACT_LOW  ->  active low (default)   
#   ADS1115_ACT_HIGH ->  active high
#adc.setAlertPol(ADS1115_ACT_LOW)
 
#   With this function the alert pin will assert, when a conversion is ready.
#   In order to deactivate, use the setAlertLimit_V function  
#adc.setAlertPinToConversionReady()

print("ADS1115 Example Sketch - Continuous Mode")
print("All values in volts")
print("")

#  If you change the compare channels you can immediately read values from the conversion 
#  register, although they might belong to the former channel if no precautions are taken. 
#  It takes about the time needed for two conversions to get the correct data. In single 
#  shot mode you can use the isBusy() function to wait for data from the new channel. This 
#  does not work in continuous mode. 
#  To solve this issue the library adds a delay after change of channels if you are in contunuous
#  mode. The length of the delay is adjusted to the conversion rate. But be aware that the output 
#  rate will be much lower that the conversion rate if you change channels frequently. 
 
def readChannel(channel):
    adc.setCompareChannels(channel)
    voltage = adc.getResult_V()
    return voltage

while True:
    voltage0 = readChannel(ADS1115_COMP_0_GND)
    voltage1 = readChannel(ADS1115_COMP_1_GND)
    voltage2 = readChannel(ADS1115_COMP_2_GND)
    voltage3 = readChannel(ADS1115_COMP_3_GND)
    print("0: {:<8.2f} 1: {:<8.2f} 2: {:<8.2f} 3: {:<8.2f}".format(voltage0, voltage1, voltage2, voltage3))
    sleep(1)
