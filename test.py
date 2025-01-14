import pyautogui
import cv2

img = cv2.imread("input.png")
img = cv2.resize(img, (500, 500), interpolation = cv2.INTER_AREA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape

# start position
sx = 100
sy = 200
num = 0
pyautogui.PAUSE = 0.01

# rows and columns
for r in range(height):
    for c in range(width):
        # black pixel -> click
        if img[r, c] == 0:
            pyautogui.click(sx+c, sy+r)
            num = num + 1

print("Clicke", num, "times")