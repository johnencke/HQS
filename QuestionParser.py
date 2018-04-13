'''



'''
#import cv2
import os
import pytesseract
import pyscreenshot as ImageGrab
from pynput.mouse import Listener
from PIL import Image
import time
import queue



def parseText(im):
	text = pytesseract.image_to_string(im)
	text = text.split('\n')
	question = ''
	answers = []
	for i in range(0, len(text)):
		if text[i] == '' and question == '':
			question = " ".join(text[0:i])
		else:
			if text[i] != '' and question != '':
				answers.append(text[i])


	#os.remove('HQ3.png')
	print('Question: ', question)
	print('Answer 1: ', answers[0])
	print('Answer 2: ', answers[1])
	print('Answer 3: ', answers[2])

'''
Takes mouse click 
returns x and y
'''

x1 = 1
y1 = 1
x2 = 2
y2 = 2 
q = queue.Queue(4)
def captureImage():
	def on_click(x, y, button, pressed):
		print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
		if pressed:
			q.put(x)
			q.put(y)
			return True
		else:
			q.put(x)
			q.put(y)
			return False
	with Listener(on_click=on_click) as listener:
		q.join()
		listener.join()
	x1 = q.get()
	y1 = q.get()
	x2 = q.get()
	y2 = q.get()
	im = ImageGrab.grab(bbox=(x1,y1,x2,y2))
	parseText(im)
	





if __name__ == '__main__':
	captureImage()


