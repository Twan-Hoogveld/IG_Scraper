from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import platform
import sys

if __name__ == '__main__':
	#Options for a headless chrome webdriver.
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument("disable-gpu")

	#Check platform.
	if platform.system() == 'Windows':
		#Webdriver for Windows
		driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe",options=options)
	else:
		#Webdriver for Linux
		driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)

	#Get the webpage and username from the CLI
	try:
		username = str(sys.argv[1])
	except IndexError:
		exit()
	driver.get("https://www.instagram.com/{}/".format(username))

	#Make it readable
	content = driver.page_source
	soup = BeautifulSoup(content,features="html.parser")

	#Find the classes containing the data we want
	data = []
	for a in soup.findAll('a',href=True, attrs={'class':'-nal3'}):
		data.append(a.find('span', attrs={'class':'g47SY'}).text)

	#Print.
	print("User : {} \nPosts : {} \nFollowers: {} \nFollowing {}".format(username,data[0],data[1],data[2]))
