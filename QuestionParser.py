'''



'''
#import cv2
import os
from PIL import Image
import pytesseract

def parseText(fileName):
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


	#os.remove('HQ3.png')
	print('Question: ', question)
	print('Answer 1: ', answers[0])
	print('Answer 2: ', answers[1])
	print('Answer 3: ', answers[2])

parseText("")


