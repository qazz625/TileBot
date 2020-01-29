import time
import pyscreenshot as pss
import cv2
import numpy as np
import pyautogui as pag

# pag.FAILSAFE=True
pag.PAUSE=0.001

add = 15
last_time = time.time()
p = time.time()
var = 0
for i in range(3000):
	flag = 0
	screen = np.array(pss.grab(bbox=(780, 300, 1220, 920)))
	x = time.time()-last_time
	# print('loop took', x, 'seconds')
	# cv2.imshow('screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	last_time = time.time()

	for y in range(398, 441):
		for x in range(116, 292):
			if screen[y][x][0] == 58 and screen[y][x][1] == 149 and screen[y][x][2] == 201 and var == 0:
				pag.click(x=x+10, y=y+add)
				var = 1
			elif screen[y][x][0] == 17 and screen[y][x][1] == 17 and screen[y][x][2] == 17 and var == 1:
				pag.click(x=x+10, y=y+add)
				flag = 1
				break
		if flag == 1:
			break
	if p-time.time() >= 20:
		add += 5
		p = time.time()
	if p-time.time() == 60:
		add += 15
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break



# blue is [58 149 201]

#116 398

#292 441