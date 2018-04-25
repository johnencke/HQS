from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
from questionParser import QuestionParser
from PIL import Image
import webbrowser
from datetime import datetime

my_api_key = "AIzaSyClRm3OS-OCShRJu6W4FJ_PhpUbDOHTMkQ"
my_cse_id = "015426465276113101398:etj8c0m8u_u"  	

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
	html_resultStats = html.find('div', id='resultStats')
	# totalResults = int(html_resultStats.prettify().split('\n')[1].split(' ')[2].replace(',', ''))
	return html_resultStats

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
	return totalResults, response

def printGoogleAPIResults(qp:QuestionParser):
	for i in range(0,3):
		results, response = googleAPITotalResults(qp.unformattedQuestion + ' ' + qp.unformattedAnswers[i])
		frequency = getFrequency(response)
		print('Answer', i + 1, "Results: ", results, "Frequency: ", frequency)	


def getFrequency(response):
	return response['items'][0]
	



if __name__ == "__main__":
	startTime = datetime.now()
	qp = QuestionParser(Image.open('Capture.png'))
	print(qp)
	print(datetime.now() - startTime, '\n')

	print ("Parsing HTML")
	startTime = datetime.now()
	printHtmlParseResults(qp)
	print(datetime.now() - startTime, '\n')
	
	print ("Google API Search")
	startTime = datetime.now()
	printGoogleAPIResults(qp)
	print(datetime.now() - startTime, '\n')