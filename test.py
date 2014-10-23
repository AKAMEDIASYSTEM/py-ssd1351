#----------------------------------------------------------------------
# ssd1351.py from https://github.com/boxysean/py-gaugette
# ported by boxysean
#
# This library works with 
#   Adafruit's 128x128 SPI RGB OLED   https://www.adafruit.com/products/1431
#
# The code is based heavily on Adafruit's Arduino library
#   https://github.com/adafruit/Adafruit-SSD1351-library
# written by Limor Fried/Ladyada for Adafruit Industries.
#
# Some important things to know about this device and SPI:
#
# SPI and GPIO calls are made through an abstraction library that calls
# the appropriate library for the platform.
# For the RaspberryPi:
#     wiring2
#     spidev
#
# Presently untested / not supported for BBBlack
#
#----------------------------------------------------------------------

import ssd1351 as ssd
import time
# Color definitions
BLACK    = 0x0000
BLUE     = 0x001F
RED      = 0xF800
GREEN    = 0x07E0
CYAN     = 0x07FF
MAGENTA  = 0xF81F
YELLOW   = 0xFFE0 
WHITE    = 0xFFFF

disp = ssd.SSD1351()
disp.begin()
c = 0

while True:
    # disp.clear_display()
    # disp.draw_text(32,32,'hey',0xF800) # should be red
    # # disp.dump_buffer()
    # # disp.data(disp.bitmap)
    # time.sleep(1)
    c = c+5000
    disp.clear_display()
    print 'red'
    disp.fillScreen(0b11111111111111110000000000000000)
    time.sleep(1)
    disp.clear_display()
    print 'green'
    disp.fillScreen(0b00000000000000001111111000000000)
    time.sleep(1)
    disp.clear_display()
    print 'blue'
    disp.fillScreen(0b00000000000000000000000011111111)
    time.sleep(1)
    # blue is 0x00ff00
    # disp.fillScreen(disp.color565(0,255,0)) # should be green
    # time.sleep(.1)