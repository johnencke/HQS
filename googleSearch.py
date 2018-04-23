from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
import questionParser
from PIL import Image

my_api_key = "AIzaSyClRm3OS-OCShRJu6W4FJ_PhpUbDOHTMkQ"
my_cse_id = "015426465276113101398:etj8c0m8u_u"

def google_search(search_term, api_key, cse_id, **kwargs):
      service = build("customsearch", "v1", developerKey=api_key)
      res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
      return res['items']

im = Image.open('hq4.png')
qp = questionParser.QuestionParser(im)

print (qp.answers)
# search_string = qp.question
# results = google_search(search_string, my_api_key,my_cse_id, num=10) 

# for result in results:
#       print(result["link"])


# response = requests.get('https://en.wikipedia.org/wiki/Soviet_Union')
# soup = BeautifulSoup(response.text, 'html.parser')

# page = soup.get_text().encode("utf-8")

# if 'Hitler'.encode("utf-8") in page:
# 	print (True)
# else:
# 	print (False)

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