from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
from questionParser import QuestionParser
from PIL import Image
import webbrowser
from datetime import datetime

my_api_key = "AIzaSyClRm3OS-OCShRJu6W4FJ_PhpUbDOHTMkQ"
my_cse_id = "015426465276113101398:etj8c0m8u_u"  	

def makeURL(search_term):
	return 'https://www.google.com/search?q=' + search_term

def googleAPITotalResults(search_term, api_key = my_api_key, cse_id = my_cse_id):
	service = build("customsearch", "v1", developerKey=api_key)
	response = service.cse().list(q=search_term, cx=cse_id).execute()
	totalResults = response['searchInformation']['totalResults']
	return totalResults


def getTotalResults(url):
	response = requests.get(url)
	html = BeautifulSoup(response.text, 'lxml')
	html_resultStats = html.find('div', id='resultStats')
	totalResults = int(html_resultStats.prettify().split('\n')[1].split(' ')[2].replace(',', ''))
	return totalResults

def googleAPIResultsAlg(qp:QuestionParser):
	for i in range(0,3):
		print('Answer', i+1, "Restults: ", googleAPITotalResults(qp.unformattedQuestion + qp.unformattedAnswers[i]))

def getResultsAlg(qp:QuestionParser):
	for i in range(0,3):
		print('Answer', i+1, "Restults: ", getTotalResults(makeURL(qp.unformattedQuestion + qp.unformattedAnswers[i])))


if __name__ == "__main__":
	startTime = datetime.now()
	qp = QuestionParser(Image.open('hq5.png'))
	print(qp)
	print(datetime.now() - startTime, '\n')
	getResultsAlg(qp)
	print(datetime.now() - startTime, '\n')
	googleAPIResultsAlg(qp)
	print(datetime.now() - startTime, '\n')