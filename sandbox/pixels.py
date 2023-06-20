#!/usr/bin/env python
import time

from base import SandboxBase
import random
from collections import deque


# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


def rand_pixel():
    x = random.randint(0, 64)
    y = random.randint(0, 64)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return x, y, r, g, b

class Pixels(SandboxBase):
    def __init__(self, *args, **kwargs):
        super(Pixels, self).__init__(*args, **kwargs)

    def run(self):

        offset_canvas = self.matrix.CreateFrameCanvas()

        items = 20
        d = deque([], items)

        i = 0
        while True:
            # a = random.randint(0, 255)
            p = rand_pixel()
            # print('in', p)
            d.append(p)
            offset_canvas.SetPixel(*p)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            if len(d) >= items:
                x, y, r, g, b = d.popleft()
                offset_canvas.SetPixel(x, y, 0, 0, 0)
            i = i + 1
            time.sleep(0.01)


# Main function
if __name__ == "__main__":
    pixels = Pixels()
    if (not pixels.process()):
        pixels.print_help()
