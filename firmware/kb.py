import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP15,
        board.GP14,
        board.GP8,
        board.GP7,
        board.GP6,
        board.GP5,
        board.GP4,
    )
    row_pins = (
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
    )
    diode_orientation = DiodeOrientation.COLUMNS

