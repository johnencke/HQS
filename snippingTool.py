'''
SnippingTool Python
Adapted from: https://github.com/harupy/snipping-tool

'''

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import questionParser
import webbrowser
import googleSearch as gs
from datetime import datetime
import threading
import time

my_api_key = "AIzaSyClRm3OS-OCShRJu6W4FJ_PhpUbDOHTMkQ"
my_cse_id = "015426465276113101398:etj8c0m8u_u"

class HqThread(threading.Thread):
    def __init__(self, q:questionParser.QuestionParser, func , startTime):
        threading.Thread.__init__(self)
        self.q = q
        self.func = func
        self.startTime = startTime
    def run(self):
        self.func(self.q)
        print(datetime.now() - self.startTime, '\n')

class ScreenCapWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('capture.png')
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

#        cv2.imshow('Captured Image', img)
#        cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #q = questionParser.QuestionParser(Image.open("hq6.png"))
        #print(q)
        #googleSearch.makeQuery(q)
        #newQ = q.question
        #newQ = "+".join(newQ.split())
        #newQ = newQ.replace("?", "")
        #newQ = newQ.lower()
        #print(newQ)

        q = questionParser.QuestionParser(img)
        if q.answers[2] != "Read Error":
            print(q)
            #print('------\n', (datetime.now() - startTime), '\n------')
            #print ("Parsing HTML")
            startTime = datetime.now()
            #gs.openWindow(q.unformattedQuestion)
            gs.printHtmlParseResults(q)
            print(datetime.now() - startTime, '\n')

        #Threading can be useful for executing all algorithms concurrently
        # t1 = HqThread(q, gs.getResultsAlg, startTime)
        # t2 = HqThread(q, gs.googleAPIResultsAlg, startTime)
        # t1.start()
        # t2.start()
        # t1.join()
        # t2.join()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ScreenCapWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
