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
RED = [255, 0, 0]
WHITE = [255, 255, 255]

faces_color = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO]


def face_xy(x, y, face=0, cols=COLS, rows=ROWS):
    return x + face * cols if x >= 0 else x + cols + face * cols, \
           y if y >= 0 else ROWS + y


# Matrix configuration :
options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.chain_length = CHAIN
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

font = graphics.Font()
font.LoadFont("./fonts/7x13.bdf")

matrix = RGBMatrix(options=options)
matrix.Clear()

canvas = matrix.CreateFrameCanvas()

for f in range(0, CHAIN):
    for x in range(0, COLS):
        canvas.SetPixel(*face_xy(x, 0, f), *faces_color[f])
        canvas.SetPixel(*face_xy(x, -1, f), *faces_color[f])
    for y in range(0, ROWS):
        canvas.SetPixel(*face_xy(0, y, f), *faces_color[f])
        canvas.SetPixel(*face_xy(-1, y, f), *faces_color[f])
    graphics.DrawText(canvas, font, *face_xy(28, 35, f), graphics.Color(*faces_color[f]), str(f))

canvas = matrix.SwapOnVSync(canvas)

while True:
    time.sleep(0.1)
