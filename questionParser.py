import os
import sys
import pytesseract
import pyscreenshot as ImageGrab
from pynput.mouse import Listener
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
import time


def parseText(im):
	text = pytesseract.image_to_string(im)
	text = correctReadErr(text)
	splitText = text.split('\n')
	question = ''
	answers = []
	# Two ways to determine where the question ends and where the answers begin
	# If text has one and only one question mark, then the question ends at the question mark
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

	print('Question: ', question)
	print('Answer 1: ', answers[0])
	print('Answer 2: ', answers[1])
	print('Answer 3: ', answers[2])


def correctReadErr(text):
	text = text.replace(u"\ufb01", "fi")
	text = text.replace(u"\ufb02", "fl")
	text = text.replace(u"\u201c", "\"")
	text = text.replace(u"\u201d", "\"")
	text = text.replace(u"\u2018", "\'")
	text = text.replace(u"\u2019", "\'")
	return text