#!/usr/bin/env python
import math
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


def xy_to_face(x, y, cols=COLS):
    """Return the face from x,y coordinates"""
    return math.floor(x / cols)

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
canvas = matrix.CreateFrameCanvas()

canvas.Clear()
red = graphics.Color(*ORANGE)
graphics.DrawLine(canvas, *face_xy(5, 5, 0), *face_xy(60, 50, 0), red)
graphics.DrawLine(canvas, *face_xy(5, 5, 1), *face_xy(60, 50, 1), red)
graphics.DrawLine(canvas, *face_xy(5, 5, 2), *face_xy(60, 50, 2), red)
graphics.DrawLine(canvas, *face_xy(5, 5, 3), *face_xy(60, 50, 3), red)
graphics.DrawLine(canvas, *face_xy(5, 5, 4), *face_xy(60, 50, 4), red)

canvas = matrix.SwapOnVSync(canvas)

while True:
    time.sleep(1)
