#####################################################################################
# Example program for the ADS1115_mPy module
#
# This program shows how to obtain results using different scales / formats.
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

adc.setVoltageRange_mV(ADS1115_RANGE_6144)
adc.setCompareChannels(ADS1115_COMP_0_GND)
adc.setMeasureMode(ADS1115_CONTINUOUS)

print("ADS1115 Example Sketch - Results in different scales / formats")
print("All results are for Channel 0 vs. GND")
print()

while True:
    voltageInMillivolt = adc.getResult_mV() 
    print("{:<33} {:<5.0f}".format("Result in Millivolt [mV]:", voltageInMillivolt))
    voltageInVolt = adc.getResult_V() 
    print("{:<33} {:<5.2f}".format("Result in Volt [V]:", voltageInVolt))

#    Get the raw result from the conversion register. The conversion register 
#    contains the conversion result of the amplified (!) voltage. This means the
#    value depends on the voltage as well as on the voltage range. E.g. if the 
#    voltage range is 6144 mV (ADS1115_RANGE_6144), +32767 is 6144 mV; if the 
#    range is 4096 mV, +32767 is 4096 mV, and so on.
    rawResult = adc.getRawResult()
    print("{:<33}".format("Raw Result:"), rawResult)

#    Scaling of the result to a different range: 
#    The results in the conversion register are in a range of -32767 to +32767
#    You might want to receive the result in a different scale, e.g. -1023 to 1023.
#    For -1023 to 1023, and if you have chosen e.g. ADS1115_RANGE_4096, 0 Volt would 
#    give 0 as result and 4096 mV would give 1023. -4096 mV would give -1023.
    scaledResult = adc.getResultWithRange(-1023, 1023)
    print("{:<33} {:<5.0f}".format("Scaled result:",scaledResult))

#    Scaling of the result to a different range plus scaling to a voltage range: 
#    You can use this variant if you also want to scale to a voltage range. E.g. in
#    in order to get results equivalent to an Arduino UNO (10 bit, 5000 mV range), you 
#    would choose getResultWithRange(-1023, 1023, 5000). A difference to the Arduino 
#    UNO is that you can measure negative voltages. 
#    You have to ensure that the voltage range you scale to is smaller than the 
#    measuring voltage range. For this example only ADS1115_RANGE_6144 would cover the 
#    scale up to 5000 mV. 
    scaledResultWithMaxVoltage = adc.getResultWithRangeAndMaxVolt(-1023, 1023, 5000) 
    print("{:<33} {:<5.0f}".format("Scaled result with voltage scale:", scaledResultWithMaxVoltage))

#    This function returns the voltage range ADS1115_RANGE_XXXX in Millivolt */
    voltRange = adc.getVoltageRange_mV()
    print("{:<33}".format("Voltage Range of ADS1115 [mV]:"), voltRange)
    print("---------------------------------------")
    sleep(2)
