'''



'''
#import cv2
import os
import sys
import pytesseract
import pyscreenshot as ImageGrab
from pynput.mouse import Listener
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
import time
import queue
import win32api, win32con, win32gui

'''


<<<<<<< HEAD
def parseText():
    text = pytesseract.image_to_string(Image.open('HQ4.png'))
    text = text.split('\n')
    question = ''
    answers = []
    for i in range(0, len(text)):
        if text[i] == '' and question == '':
            question = " ".join(text[0:i])
        else:
            if text[i] != '' and question != '':
                answers.append(text[i])

    print('Question: ', question)
    print('Answer 1: ', answers[0])
    print('Answer 2: ', answers[1])
    print('Answer 3: ', answers[2])

parseText()
=======
'''
def parseText(im):
	text = pytesseract.image_to_string(im)
	text = correctReadErr(text)
	splitText = text.split('\n')
	question = ''
	answers = []
	#Two ways to determine where the question ends and where the answers begin
	#If text has one and only one question mark, then the question ends at the question mark
	if text.count("?") == 1:
		for i in range(0, len(splitText)):
			if splitText[i].count('?') == 1 and question == '':
				question = " ".join(splitText[0:(i+1)])
			else:
				if splitText[i] != '' and question != '':
					answers.append(splitText[i])

	else:
		for i in range(0, len(splitText)):
			if splitText[i] == '' and question == '':
				question = " ".join(splitText[0:i])
			else:
				if splitText[i] != '' and question != '':
					answers.append(splitText[i])
	
	while (len(answers)<=3):
		answers.append("Read Error")

	#os.remove('HQ3.png')
	print('Question: ', question)
	print('Answer 1: ', answers[0])
	print('Answer 2: ', answers[1])
	print('Answer 3: ', answers[2])


def correctReadErr(text):
	text = text.replace(u"\ufb01", "fi")
	text = text.replace(u"\u201c", "\"")
	text = text.replace(u"\u201d", "\"")
	text = text.replace(u"\u2018", "\'")
	text = text.replace(u"\u2019", "\'")
	return text


'''
Takes mouse click 
returns x and y


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
			q2.put(x)
			q2.put(y)
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
	im.show()
	parseText(im)
'''

if __name__ == '__main__':
	parseText()
>>>>>>> 84e7f70eea7f47bd802c73cea2b3bc4931d73f7a


