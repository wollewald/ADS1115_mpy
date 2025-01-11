# ADS1115_mpy
A MicroPython module for the 16-bit, 4 channel ADS1115 and ADS1015 ADC. All features of the ADS1x15 are implemented, including alert functions.

I have developed it on the ESP32, latest successful test was with the firmware version v1.24.1 (2024-11-29). 

I have have tried to optimize the module for convenience to use. If you try the examples I recommend 
to start with ads1115_single_shot.py. 

All features of the ADS1115 are implemented, including alert functions. 

The module is a translation of my Arduino library ADS1115_WE which you find here on GitHub:

https://github.com/wollewald/ADS1115_WE 

You can find more information about the ADS1115 in my blog post about the Arduino version:  

https://wolles-elektronikkiste.de/ads1115 (German)

https://wolles-elektronikkiste.de/en/ads1115-a-d-converter-with-amplifier (English)

<h3>ADS1115 or ADS1015 - which ADC do you really have?</h3>

There are many modules which are labelled as ADS1115 which are based on an ADS1015 and the other way round. The main differences are:

ADS1115: 16-bit resolution / 8 SPS to 860 SPS

ADS1015: 12-bit resolution / 128 SPS to 3300 SPS

You might not even notice if have not the one you thought you have. To find out which one you have, you can use ads1115_who_am_i.py.
