#!/usr/bin/env python
import time

import graphics
from base import SandboxBase
import random
from collections import deque
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions

COLS = 64
ROWS = 64
CHAIN = 6

VIOLET = [148, 0, 211]
INDIGO = [75, 0, 130]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
YELLOW = [255, 255, 0]
ORANGE = [255, 127, 0]
RED = [255, 0 , 0]
WHITE = [255, 255, 255]

faces_color = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO]

# Matrix configuration :
options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.chain_length = CHAIN
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

font = graphics.Font()
font.LoadFont("./fonts/iv9x16u.bdf")

matrix = RGBMatrix(options=options)
matrix.Clear()

canvas = matrix.CreateFrameCanvas()

for face in range(0, CHAIN):
    for x in range(0, COLS):
        canvas.SetPixel(x + face * COLS, 0, *faces_color[face])
        canvas.SetPixel(x + face * COLS, ROWS - 1, *faces_color[face])
    for y in range(0, matrix.height):
        canvas.SetPixel(face * COLS, y, *faces_color[face])
        canvas.SetPixel(face * COLS + COLS - 1, y, *faces_color[face])
    graphics.DrawText(canvas, font, face * 64 + 28, 35, graphics.Color(*faces_color[face]), str(face))

canvas = matrix.SwapOnVSync(canvas)

while True:
    time.sleep(0.1)
