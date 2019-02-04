import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from selenium import webdriver
import urllib.request
import time

class Window(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Image Grabber")
		self.setGeometry(100,100,400,200)
		vbox = QVBoxLayout()
		self.label = QLabel("Image Grabber")
		self.label.setFont(QtGui.QFont("serif",20))
		hbox = QHBoxLayout()
		self.url_lineedit = QLineEdit(self)
		self.url_lineedit.setText("url")
		self.item_count_lineedit = QLineEdit(self)
		self.item_count_lineedit.setText("how many images do you want ?")
		self.submit_btn = QPushButton("submit")
		self.submit_btn.clicked.connect(self.submit)

		vbox.addWidget(self.label)
		hbox.addWidget(self.url_lineedit)
		hbox.addWidget(self.item_count_lineedit)
		vbox.addLayout(hbox)
		vbox.addWidget(self.submit_btn)
		self.setLayout(vbox)
		self.show()


	def submit(self):
		driver = webdriver.Chrome()
		url = self.url_lineedit.text()
		item_count = int(self.item_count_lineedit.text())

		driver.get(url)
		counter =0
		while counter < item_count : 
			time.sleep(3)
			driver.execute_script("window.scrollTo(0, window.scrollY + 1000);")
			images = driver.find_elements_by_tag_name('img')
			for image in images:
				try:
					src = image.get_attribute('src')
					urllib.request.urlretrieve(src, str(counter) + ".jpg")
					counter +=1
				except:
					break
				


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())