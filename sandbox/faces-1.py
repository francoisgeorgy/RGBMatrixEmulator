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

for i in range(6):
    graphics.DrawText(matrix, font, i*64 + 28, 35, textColor, str(i))
# graphics.DrawText(matrix, font, 1*64, 12, textColor, "2")
# graphics.DrawText(matrix, font, 2*64, 12, textColor, "3")
# graphics.DrawText(matrix, font, 3*64, 12, textColor, "4")
# graphics.DrawText(matrix, font, 4*64, 12, textColor, "5")
# graphics.DrawText(matrix, font, 5*64, 12, textColor, "6")

while True:
    time.sleep(0.1)
