import os
import sys
import pytesseract
from PIL import Image
import time

class QuestionParser:

	def __init__(self, im):
		self.question = ''
		self.answers = []
		self.__parseText(im)

	def __parseText(self, im):
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
		
		while (len(self.answers)<=3):
			self.answers.append("Read Error")

	def __str__(self):
		return 'Question: ' + self.question + '\nAnswer 1: ' + self.answers[0] + '\nAnswer 2: ' + self.answers[1] + '\nAnswer 3: ' + self.answers[2]


	def __correctReadErr(self, text):
		text = text.replace(u"\ufb01", "fi")
		text = text.replace(u"\ufb02", "fl")
		text = text.replace(u"\u201c", "\"")
		text = text.replace(u"\u201d", "\"")
		text = text.replace(u"\u2018", "\'")
		text = text.replace(u"\u2019", "\'")
		return text

