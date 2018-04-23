import os
import sys
import pytesseract
from PIL import Image
import time

class QuestionParser:
	'''Question Parser Object'''
	def __init__(self, im:Image):
		'''
		Take in image 
		'''
		self.question = ''
		self.answers = []
		self.__parseText(im)

	def __parseText(self, im:Image):
		'''
		Private method that reads image using pytesserct and sets self.queston and self.answers
		'''
		text = pytesseract.image_to_string(im)
		text = self.__correctReadErr(text)
		splitText = text.split('\n')
		# Two ways to determine where the question ends and where the answers begin
		# If text has one and only one question mark, then the question ends at the question mark
		if text.count("?") == 1:
			for i in range(0, len(splitText)):
				if splitText[i].count('?') == 1 and self.question == '':
					self.question = " ".join(splitText[0:(i+1)])
				else:
					if splitText[i] != '' and self.question != '':
						self.answers.append(splitText[i])

		else:
			for i in range(0, len(splitText)):
				if splitText[i] == '' and self.question == '':
					self.question = " ".join(splitText[0:i])
				else:
					if splitText[i] != '' and self.question != '':
						self.answers.append(splitText[i])
		
		while (len(self.answers) < 3):
			self.answers.append("Read Error")

	def __str__(self):
		'''To String method that prints the question and the three answers'''
		return 'Question: ' + self.question + '\nAnswer 1: ' + self.answers[0] + '\nAnswer 2: ' + self.answers[1] + '\nAnswer 3: ' + self.answers[2]


	def __correctReadErr(self, text):
		'''Called in __parseText. Corrects common read errors from pytesseract'''
		text = text.replace(u"\ufb01", "fi")
		text = text.replace(u"\ufb02", "fl")
		text = text.replace(u"\u201c", "\"")
		text = text.replace(u"\u201d", "\"")
		text = text.replace(u"\u2018", "\'")
		text = text.replace(u"\u2019", "\'")
		return text

