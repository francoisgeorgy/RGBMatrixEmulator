from RGBMatrixEmulator.adapters.pygame_adapter import PygameAdapter
from RGBMatrixEmulator.adapters.terminal_adapter import TerminalAdapter
from RGBMatrixEmulator.adapters.tkinter_adapter import TkinterAdapter
from RGBMatrixEmulator.adapters.turtle_adapter import TurtleAdapter

ADAPTER_TYPES = {
    'pygame':   PygameAdapter,
    'terminal': TerminalAdapter,
    'tkinter':  TkinterAdapter,
    'turtle':   TurtleAdapter
}