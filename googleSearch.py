from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
from questionParser import QuestionParser
from PIL import Image
import webbrowser
from datetime import datetime

my_api_key = 'AIzaSyClRm3OS-OCShRJu6W4FJ_PhpUbDOHTMkQ'
my_cse_id = '015426465276113101398:etj8c0m8u_u' 	

my_api_key2 = 'AIzaSyAxBsoRzCvsv0mXlsHX7Pw846KWxpNqx4g'
my_cse_id2 = '002815009267709723541:nkrdgvsmczu'

my_cse_id3 = '015426465276113101398:xj_pxu5xibw'

my_api_key4 = "AIzaSyBr_1D-usLPDE50lQm0QVUnQqZ8qkEl6fg"
my_cse_id4 = "002815009267709723541:epubpgzcgog"

EXCLUDE_THESE = ['these','those', 'does', "also", "who", "what", "when", "where", "why", "how","for", "is", "was", "are", "isn't", "aren't", "wasn't", "will", "won't", \
"where", "that", "there", "the", "a", "an", "which", "of", "A", "in"]


"""
Generates and returns URL based on the search query
"""
def makeURL(search_term):
	return 'https://www.google.com/search?q=' + search_term


"""
Using HTML parsing, it returns number of results that the search yields
"""
def htmlParseTotalResults(url):
	response = requests.get(url)
	html = BeautifulSoup(response.text, 'lxml')
	resultStatsString = html.find('div', id='resultStats').string
	return resultStatsString

def printHtmlParseResults(qp:QuestionParser):
	for i in range(0,3):
		print('Answer', i + 1, "Results: ", htmlParseTotalResults(makeURL(qp.unformattedQuestion + ' ' + qp.unformattedAnswers[i])))


"""
Using Google's Custom Search API, it returns the number of results that each search yields
"""
def googleAPITotalResults(search_term, api_key = my_api_key, cse_id = my_cse_id):
	service = build("customsearch", "v1", developerKey=api_key)
	response = service.cse().list(q=search_term, cx=cse_id).execute()
	totalResults = response['searchInformation']['totalResults']
	return totalResults

def googleAPIResponse(search_term, api_key = my_api_key, cse_id = my_cse_id):
	service = build("customsearch", "v1", developerKey=api_key)
	return service.cse().list(q=search_term, cx=cse_id).execute()


def getFrequency(response, answer):
	count = 0
	try:
		for i in range(0, len(response['items'])):
			count += response['items'][i]['snippet'].lower().count(answer)
		return count
	except KeyError:
		return -1

def printGoogleAPIResults(qp:QuestionParser):
	keywords = removeCommonWords(qp.question.lower())
	for i in range(0, 3):
		results = googleAPITotalResults(qp.unformattedQuestion + ' ' + qp.unformattedAnswers[i])
		questionResponse = googleAPIResponse(qp.unformattedQuestion)
		frequencyAnswer = getFrequency(questionResponse, qp.answers[i].lower())
		answerResponse = googleAPIResponse(qp.unformattedAnswers[i])
		frequencyQuestion = 0
		for word in keywords:
			frequencyQuestion += getFrequency(answerResponse, word)
		print('Answer', i + 1, "Results: ", results, "Frequency of Answer in Question: ", frequencyAnswer, "Frequency of Question Keywords in Answer: ", frequencyQuestion)

def removeCommonWords(statement):
	statement = statement[:-1]
	statement = statement.split(" ")
	print (statement)
	for word in statement:
		if word in EXCLUDE_THESE:
			statement.remove(word)
	print(statement)
	return statement


if __name__ == "__main__":
	startTime = datetime.now()
	file = input('File: ')
	qp = QuestionParser(Image.open("4_25_2018/" + file + ".png"))
	print(qp.unformattedQuestion)
	print(qp.unformattedAnswers)
	print(datetime.now() - startTime, '\n')

	print ("Parsing HTML")
	startTime = datetime.now()
	printHtmlParseResults(qp)
	print(datetime.now() - startTime, '\n')
	
	print ("Google API Search")
	startTime = datetime.now()
	printGoogleAPIResults(qp)
	print(datetime.now() - startTime, '\n')