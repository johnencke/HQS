Project: HQ Trivia Solver

Team Members: Andrew Altadonna, John Encke, Robert Salewski, Joshua Smith

Github Link: https://github.com/johnencke/HQS

Scope:
This project will use Python to win the popular HQ Trivia app. 
In the game, the player only has 10 seconds to answer a multiple choice 
question. It is very difficult for the player to research the answer on 
their own. This program will read the question and choices using optical 
character recognition. In order for the app to be able to read the question, 
the players iPhone will be mirrored on the computer running the py file. 
The user will need to quickly screenshot the question. 
The question will be parsed to take out any extraneous words. 
Then, the program will use Google to find the answer that is most associated 
with the question and output that answer to the user.

Python Packages:
Pytesseract for optical character recognition
BeautifulSoup for web scraping
Google for googling
Pyscreenshot for capturing the screen


Resources:
https://www.geeksforgeeks.org/performing-google-search-using-python-code/
https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
https://pypi.python.org/pypi/tesserocr
https://pypi.python.org/pypi/pyscreenshot
https://medium.com/@LtHummus/building-the-ultimate-hq-bot-c8f89a120fe2
