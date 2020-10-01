from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

username = "twanhoogveld"
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)
driver.get("https://www.instagram.com/{}/".format(username))

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")

data = []
for a in soup.findAll('a',href=True, attrs={'class':'-nal3'}):
	data.append(a.find('span', attrs={'class':'g47SY'}).text)

print("Posts : {}".format(data[0]))
print("followers : {}".format(data[1]))
print("following : {}".format(data[2]))
