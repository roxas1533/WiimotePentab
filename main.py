import clr
from ctypes import *
from time import *

user32 = windll.user32


class POINT(Structure):
    _fields_ = [("X", c_int32),
                ("Y", c_int32)]


def leftClick():
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    sleep(0.1)
    user32.mouse_event(0x0004, 0, 0, 0, 0)


user32.GetCursorPos.restype = c_bool
user32.GetCursorPos.argtypes = (POINTER(POINT),)
pt = POINT()

clr.AddReference("WiimoteLib")

from WiimoteLib import *

wii = Wiimote()


def get_value(sender, args):
    global a
    a = args


wii.WiimoteChanged += WiimoteChangedEventHandler(get_value)

wii.Connect()
wii.SetReportType(wii.InputReport.IRAccel, True)
# wii.SetReportType(wii.ButtonsAccel, True)
# wii.SetRumble(False)
wii.SetLEDs(0b0000)
b = WiimoteState()
speed = 20
while True:
    # print(a.WiimoteState.IRState.X1)
    user32.SetCursorPos(int(a.WiimoteState.IRState.X1 * 1366), int(1.0-a.WiimoteState.IRState.Y1 * 768))
    if a.WiimoteState.ButtonState.B:
        exit(0)
    # user32.GetCursorPos(pt)
    # if a.WiimoteState.ButtonState.Left:
    #     user32.SetCursorPos(int(pt.X - 10), pt.Y)
    # if a.WiimoteState.ButtonState.Right:
    #     user32.SetCursorPos(int(pt.X + 10), pt.Y)
    # if a.WiimoteState.ButtonState.Up:
    #     user32.SetCursorPos(pt.X, int(pt.Y - 10))
    # if a.WiimoteState.ButtonState.Down:
    #     user32.SetCursorPos(pt.X, int(pt.Y + 10))
    # if a.WiimoteState.ButtonState.A:
    #     leftClick()
    # if a.WiimoteState.ButtonState.Plus:
    #     speed += 1
    # if a.WiimoteState.ButtonState.Minus:
    #     speed -= 1
    sleep(0.016666)
