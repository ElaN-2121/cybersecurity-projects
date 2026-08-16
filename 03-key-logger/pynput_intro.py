'''
pynput package: used for input streams, helps us control our keyboard and mouse

pynput 

# controls the mouse
# listens to your mouse
# controls keyboard
# listens to your keyboard 
'''

from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlMouse():
    mouse = Controller()
    mouse.position = (10,20) # 10 from left 20 from top - top to bottom - left to right

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("under da see")

controlKeyboard()

