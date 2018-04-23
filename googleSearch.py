try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
def makeQuery(qp):
	query = qp.question

	for i in search(query, tld="com", num=10, stop=1, pause=2):
   	 print(i)