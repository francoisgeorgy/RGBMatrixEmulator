#!/usr/bin/env python
import time

from base import SandboxBase
import random
from collections import deque
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions


COLS = 64
ROWS = 64
CHAIN = 3


def rand_pixel():
    x = random.randint(0, COLS * CHAIN)
    y = random.randint(0, ROWS)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return x, y, r, g, b


# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = ROWS
options.cols = COLS
options.chain_length = CHAIN
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)
matrix.Clear()

items = 20
d = deque([], items)

i = 0
while True:
    p = rand_pixel()
    # print('in', p)
    d.append(p)
    matrix.SetPixel(p[0], p[1], p[2], p[3], p[4])
    # matrix = matrix.SwapOnVSync(matrix)
    if len(d) >= items:
        x, y, r, g, b = d.popleft()
        matrix.SetPixel(x, y, 0, 0, 0)
    i = i + 1
    time.sleep(0.01)
