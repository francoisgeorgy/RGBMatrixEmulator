#!/usr/bin/env python
import math
import time

import graphics
from base import SandboxBase
import random
from collections import deque
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions

# https://www.enjoyalgorithms.com/blog/rotate-a-matrix-by-90-degrees-in-an-anticlockwise-direction

# replace (x,y) with (−y,x). That will rotate 90 degrees counterclockwise about the origin.
#
# What you proposed will flip everything around a 45-degree line that runs from southeast to northwest.
#
# BTW: To rotate clockwise, replace (x,y) with (y,−x)
#
#     A0,0   B1,0   C2,0   D3,0
#     E0,1   F1,1   G2,1   H3,1
#     I0,2   J1,2   K2,2   L3,2
#     M0,3   N1,3   O2,3   P3,3
#
# 90 degree CCW:
#
#     D0,0   H1,0   L2,0   P3,0
#     C0,1   G1,1   K2,1   O3,1
#     B0,2   F1,2   J2,2   N3,2
#     A0,3   E1,3   I2,3   M3,3
#
#  w = 3, h = 3   max coord for width and height
#
#  0,0 --> 0,3    x1 = y0  y1 = h - x0
#  3,0 --> 0,0             y1 = 3 - 3 = 0
#  1,3 --> 3,2             y1 = 3 - 1 = 2
#
# 90 degree CW:
#
#     M0,0   I1,0   E2,0   A3,0
#     N0,1   J1,1   F2,1   B3,1
#     O0,2   K1,2   G2,2   C3,2
#     P0,3   L1,3   H2,3   D3,3
#
#  w = 3, h = 3   max coord for width and height
#
#  0,0 --> 3,0    y1 = x0  x1 = w - y0
#  3,0 --> 3,3             x1 = 3 - 0 = 3
#  1,3 --> 0,1             x1 = 3 - 3 = 0
#

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


def rotate_ccw_90(x, y, width=COLS):
    return y, width - 1 - x


def rotate_cw_90(x, y, width=COLS):
    return width - 1 - y, x


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

i = 0
while True:
    canvas.Clear()
    for x in range(0, CHAIN * COLS):
        y = round((math.sin((x + i)/10) / 2 + 0.5) * (ROWS-1))
        f = xy_to_face(x, y)
        if f == 1:
            xr, yr = rotate_ccw_90(x - f*COLS, y)
            canvas.SetPixel(xr + f*COLS, yr, *faces_color[f])
        elif f == 3:
            xr, yr = rotate_cw_90(x - f*COLS, y)
            canvas.SetPixel(xr + f*COLS, yr, *faces_color[f])
        else:
            canvas.SetPixel(x, y, *faces_color[f])
    canvas = matrix.SwapOnVSync(canvas)
    i = i + 1
    time.sleep(0.01)
