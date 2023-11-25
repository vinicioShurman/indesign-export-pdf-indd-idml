import pyautogui
import time

# Get the screen width and height
screen_width, screen_height = pyautogui.size()

# Area of the screen in percentage
x_finish = 0.5
y_finish = 1

# Transforming percentage in int value
x_pixel_width = int(x_finish * screen_width)
y_pixel_height = int(y_finish * screen_height)

iml = pyautogui.screenshot(region=(0 ,0 ,x_pixel_width,y_pixel_height))
iml.save(r"C:\Users\vinic\Documents\Python\export-pdf-indd-idml\test\savedimg.png")
