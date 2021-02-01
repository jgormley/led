# utility package for using the LED strip and grid
import time
import board
import neopixel
import sys


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 316

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False #, pixel_order=ORDER
)

#instantiate the grid
grid_size = 16
grid = [[0] * grid_size for i in range(grid_size)]

x = 0
y = 0
x_increment = 1
for i in range(256):
    #print(f'x={x}, y={y}, i={i}')
    grid[x][y] = i + 60
    #y += y_increment
    if (i != 0 and (i+1) % (grid_size) == 0):
        #print('incrementing y')
        y += 1
        x_increment *= -1
    else:
        x += x_increment


# draw a diagonal line with a color for the line, above the line, and below the line
def diagonal(line_color=(255, 255, 255), above_color=(0, 255, 0), below_color=(0, 0, 255)):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (x == y):
                pixels[grid[x][y]] = line_color
            elif (x > y):
                pixels[grid[x][y]] = below_color
            else:
                pixels[grid[x][y]] = above_color
    pixels.write()


# render an american flag
def flag():
    # draw the stripes
    BLUE = (0, 0, 180)
    WHITE = (80, 80, 80)
    RED = (80, 0, 0)
    stripes = [RED, RED, WHITE, WHITE]
    for x in range(grid_size):
        for y in range(grid_size):
            pixels[grid[x][y]] = stripes[y % 4]

    # blue box
    for x in range(8):
        for y in range(8):
            pixels[grid[x][y+8]] = BLUE

    # stars
    for y in range(9, 15, 1):
        for x in range((y%2)+1, 7, 2):
            pixels[grid[x][y]] = WHITE

    #write it all out
    pixels.write()


# spiral down to the center
def spiral():
    #define our cardinal directions
    EAST = [1, 0]
    NORTH = [0, 1]
    WEST = [-1, 0]
    SOUTH = [0, -1]
    directions = [EAST, NORTH, WEST, SOUTH]
    direction_index = 0
    current_direction = EAST

    #start with an empty grid with all elements marked as False.  As we turn pixels on, we'll set the value to True
    g = [[False] * grid_size for i in range(grid_size)]
    # starting position
    x = 0
    y = 0
    pixel_color = 0

    while True:
        if g[x][y] == True:
            # if the next pixel to draw is already drawn, then we can break out of the loop
            break
        pixels[grid[x][y]] = (pixel_color, 255-pixel_color, pixel_color) #wheel(pixel_color) #(0, 0, 255)
        pixel_color += 1
        g[x][y] = True
        pixels.write()

        # if the next location is not valid, then change direction
        # by checking if we're within the grid boundaries first, we avoid the possibility of an index-out-of-range error with the last check 
        # because Python short-circuits on the first false statement
        if not (x+current_direction[0] < grid_size 
            and x+current_direction[0] >= 0 
            and y+current_direction[1] < grid_size 
            and y+current_direction[1] >= 0 
            and g[x+current_direction[0]][y+current_direction[1]] == False):
            
            direction_index += 1
            current_direction = directions[direction_index % 4]
        
        # set the next pixel location
        x += current_direction[0]
        y += current_direction[1]



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def clear():
    pixels.fill((0, 0, 0))
    pixels.write()


#render out the grid of x,y coordinates and their corresponding led index
#this anchors the 0,0 location in the lower-left of the output for visual ease
def printGrid():
    #for row in grid:
    #    print(' '.join([(f'{elem:4}') for elem in row]))
    #print('')
    for y in range(15, -1, -1):
        row = ''
        for x in range(16):
            row += (f'{grid[x][y]:4}')
        print(row)



# handle the command line params

if (len(sys.argv[1]) > 1):
    command = sys.argv[1]
    if command == 'clear': 
        clear()
    elif command == 'flag':
        flag()
    elif command == 'spiral':
        spiral()
    elif command == 'diagonal':
        diagonal()

