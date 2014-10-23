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

# import Adafruit_BBIO.GPIO as gpio
# import Adafruit_BBIO.SPI as spi
# import font5x8
import sys
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
# disp.clear_display()

while True:
    # disp.clear_display()
    # disp.fillScreen(0xFF0000) # green
    # disp.fillScreen(0xFF0000) # should be GB 
    # disp.fillScreen(disp.color565(255,0,0)) # should be red
    # disp.fillScreen(0xFF000000) # nothing
    # disp.fillScreen(0xFF) # like, backlight lit but black
    # disp.fillScreen(0xF0F0F0)

    # time.sleep(0.5)


    disp.clear_display()
    # disp.draw_text(32,32,'hey',disp.color565(0,0,255)) # should be blue
    disp.draw_text(32,32,'hey',WHITE) # should be green
    # disp.dump_buffer()
    # disp.data(disp.bitmap)
    time.sleep(1)

    disp.clear_display()
    disp.fillScreen(WHITE)
    # blue is 0x00ff00
    # disp.fillScreen(disp.color565(0,255,0)) # should be green
    time.sleep(0.5)

    # disp.clear_display()
    # disp.fillScreen(0x0000FF) # colors are G B R order?!
    # time.sleep(0.5)