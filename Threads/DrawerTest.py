import random
import clr

clr.AddReference('GDIDrawer')

from GDIDrawer import CDrawer
from GDIDrawer import RandColor

def GDITester():
    canvas = CDrawer()
    canvas.ContinuousUpdate = False
    for x in range(10):
        col = RandColor.GetColor()
        radius = random.randint(20,200)
        canvas.AddCenteredEllipse(
            random.randint(radius, canvas.ScaledWidth - radius),
            random.randint(radius, canvas.ScaledHeight - radius),
            radius * 2, radius * 2, col)
        canvas.Render()
        canvas.KeyboardEvent += CanvasKeyboardCallback

def CanvasKeyboardCallback(IsDown, KeyCode, canvas):
    print(f"IsDown: {IsDown}, keycode: {KeyCode}")

GDITester()
input()