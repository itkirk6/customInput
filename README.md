
# customInput

This is a wrapper for pyautogui that includes more functions and useful shortcuts. It also includes pydirectinput-rgx to allow it to interface with all applications.

## Prerequisites

```cmd
  pip install pyautogui==0.9.54
  pip install pydirectinput-rgx==1.0.4
  pip install pillow==10.3.0
  pip install opencv-python==4.9.0.80
```
    
## Functions
```python
#initialization
def __init__(safe_space=False, click_delay=False, region=False, pathToImages=pathToImages):

# waits until image is on screen or until max time limit is reached
def wait_until(description, max=20, wait=0, visible=True):

# takes a pyscreeze.Box and returns the center coordinates
def locate(object):

# moves the mouse back to the safe space
def move_back():

#finds an image on the screen and returns a Box object (x, y, length, width) or False
def find(description, confidence=None, grayscale=False):

#click an object on the screen. optionally, move back to safe_space
def click(object=None, button="left", wait=0, back=False, confidence=None):

#moves to an object
def moveTo(object, duration=0):

#presses one key
def press(key, presses=1, interval=0.1):

#presses a sequence of keys
def write(message, interval=0.1, end=""):

#pushes keys down in a sequence and then up in a reverse sequence
def hotkey(*keys):

#swipes from start to end
def swipe(start, end, duration=.25, back=False):

#scrolls a certain distance (somewhat unreliable)
def scroll(direction, distance=1, min_interval=0.04):
```



## Examples

Initialize the controller, telling it to look at only a certain section of the screen.
Wait for an "app-icon" to appear and then click on it and wait until the screen stops loading.
```python
from customInput import customInput

controller = customInput(region=(100, 100, 600, 1100))
# pyautogui will only search within (100, 100) and (600, 1100)

icon = controller.wait_until("app_icon")    # wait until "app_icon" image appears
controller.click(icon)

controller.wait_until("loading_screen", visible=False)
```

Humanlike setup: Initialize the controller, telling it to wait between moving and clicking. Make some function calls, but at a non-robotic speed.
```python
from customInput import customInput
controller = customInput(click_delay=0.5)   #wait 0.5s before clicking

controller.click("desktop_button")
controller.wait_until("desktop_loaded_indicator")
controller.click(controller.wait_until("open_application"), wait=5)
#waits 5 seconds after funciton call

controller.write("This writes as if coming from the keyboard!", end="enter")
# automatic interval of ~0.1 between keypresses
```