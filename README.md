# ADS1115_mpy
A MicroPython module for the 16-bit, 4 channel ADS1115 ADC. All features of the ADS1115 are implemented, including alert functions.

I have developed it on the ESP32, using the firmware version esp32-20210623-v1.16.bin. I will also 
try it on other boards soon. 

I have have tried to optimize the module for convenience to use. If you try the examples I recommend 
to start with ads1115_single_shot.py. 

All features of the ADS1115 are implemented, including alert functions. 

The module is a translation of my Arduino library ADS1115_WE which you find here on GitHub:

https://github.com/wollewald/ADS1115_WE 

A tutorial is not yet ready. For the moment you can find more information about the ADS1115 in my blog post 
about the Arduino version:  

https://wolles-elektronikkiste.de/ads1115 (German)

https://wolles-elektronikkiste.de/en/ads1115-a-d-converter-with-amplifier (English)

It seems there are fake modules out there which do not have the full 16 bit resolution. It's not an issue of this module:
https://github.com/wollewald/ADS1115_WE/issues/15
