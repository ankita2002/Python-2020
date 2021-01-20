import pyautogui
from os import chdir, path 

chdir(path.join(path.expanduser('~'), 'Desktop'))

pic = pyautogui.screenshot()
pic.save("Screenshot.png")
print("Screenshot Saved Sucessfully in desktop")