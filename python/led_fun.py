# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 316

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False #, pixel_order=ORDER
)

steps = 16

# r = range of pixels to iterate over
# c = color to set the pixels
def sequence(r, c):
    for i in r:
        #pixels[i] = c
        # set the next *steps* pixels too
        for j in range(steps):
            if(i+j < num_pixels and i+j >= 0):
                pixels[i+j] = c
        pixels.write()
        #time.sleep(.1)


#sequence(range(0, num_pixels, steps), (255, 0, 0))

#sequence(range(num_pixels, -1, -steps), (0, 255, 0))

#sequence(range(0, num_pixels, steps), (0, 0, 255))

#sequence(range(num_pixels, -1, -steps), (255, 255, 255))

#sequence(range(0, num_pixels, steps), (0, 0, 0))


while True:

    sequence(range(60, num_pixels, steps), (255, 0, 0))

    sequence(range(num_pixels, 60, -steps), (0, 255, 0))

    sequence(range(60, num_pixels, steps), (0, 0, 255))

    sequence(range(num_pixels, 60, -steps), (255, 255, 255))

    sequence(range(60, num_pixels, steps), (0, 0, 0))

    sequence(range(num_pixels, 60, -steps), (200, 10, 20))
