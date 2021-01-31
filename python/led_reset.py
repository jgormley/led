# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
 
# The number of NeoPixels
num_pixels = 316

pixels = neopixel.NeoPixel(board.D18, num_pixels)
pixels.fill((0,0,0))


