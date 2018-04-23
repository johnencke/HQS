from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
import questionParser
from PIL import Image
import webbrowser

my_api_key = "AIzaSyClRm3OS-OCShRJu6W4FJ_PhpUbDOHTMkQ"
my_cse_id = "015426465276113101398:etj8c0m8u_u"  	

def googleAPITotalResults(search_term, api_key, cse_id):
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




# try:
#     from googlesearch import search
# except ImportError: 
#     print("No module named 'google' found")
 
# def makeQuery(qp):
# 	query = qp.question

# 	for i in search(query, tld="com", num=10, stop=1, pause=2):
#    	 print(i)

# im = Image.open('hq4.png')

# makeQuery(questionParser.QuestionParser(im))