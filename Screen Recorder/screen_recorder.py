import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

frmat = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("test.mp4", frmat, 30.0, dim)

curr_start_time = time.time()
durn = 10+3 #3 extra sec since the code will require some time to execute 
finish_time = curr_start_time + durn

while True:
    img = pyautogui.screenshot()
    frame_one = np.array(img)
    frame = cv2.cvtColor(frame_one, cv2.COLOR_BGR2RGB)

    output.write(frame)

    curr_time = time.time()

    if curr_time > finish_time:
        break

output.release()
print("----- Khatam Tata Bye Bye, Good Bye gaya -----")















    

