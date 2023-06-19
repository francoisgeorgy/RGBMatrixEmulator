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


# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.chain_length = CHAIN
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'


font = graphics.Font()
font.LoadFont("./fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 0)

matrix = RGBMatrix(options=options)
matrix.Clear()

# for i in range(6):
#     graphics.DrawText(matrix, font, i*64 + 28, 35, textColor, str(i))

canvas = matrix.CreateFrameCanvas()

for face in range(0, CHAIN):
    for x in range(0, COLS):
        canvas.SetPixel(x + face * COLS, 0, 200 + 10 * face, 255, 255)
        canvas.SetPixel(x + face * COLS, ROWS - 1, 2 + 10 * face, 255, 255)
    for y in range(0, matrix.height):
        canvas.SetPixel(face * COLS, y, 255, 255, 255)
        canvas.SetPixel(face * COLS + COLS - 1, y, 255, 255, 255)
    graphics.DrawText(canvas, font, face * 64 + 28, 35, textColor, str(face))

canvas = matrix.SwapOnVSync(canvas)

# for x in range(0, matrix.width):
#     offset_canvas.SetPixel(x, 0, 255, 0, 0)
#     offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

while True:
    time.sleep(0.1)
