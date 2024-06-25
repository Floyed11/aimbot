import pyautogui
import time

# 移动鼠标到屏幕中央
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2, duration=1)

# 移动鼠标到指定位置 (x=100, y=200)
pyautogui.moveTo(100, 200, duration=1)

# # 鼠标单击
# pyautogui.click()

# # 鼠标右键单击
# pyautogui.rightClick()

# # 鼠标双击
# pyautogui.doubleClick()

# # 鼠标拖动
# pyautogui.dragTo(300, 300, duration=1)
