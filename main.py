import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle ( url ):
	site  = urlopen(url)
	page  = BeautifulSoup(site, 'html.parser')
	title = page.find('title').string
	return title[:-10] #because the last 10 chars always are " - YouTube"

def downloadFile ( url, fileName ):
	os.system("yt-dlp.exe -t mp3 --no-warnings -q --progress -o " + fileName + ' ' + url)




os.system("yt-dlp.exe -U -q")

downloadInfos = []

urls = open("_toDownload.txt", 'r')
for url in urls:
	title = getTitle(url)
	print(title)
	print("Name of File = ", end='')
	fileName = input()
	downloadInfos.append([url, fileName])

urls.close()

for info in downloadInfos:
	downloadFile(info[0], info[1])


# url  = "https://example.com"








# url  = "https://youtu.be/1COE-eZo6gg?si=HZp3Ep9Zkv0WOTKb"
# title = getTitle(url)
# print(title)
# downloadFile(url)







# print(url)
# site = urlopen(url)
# page = BeautifulSoup(site, 'html.parser')

# # print(page.prettify())
# print(page.find_all('title'))













# from urllib.request import urlopen
# from lxml import etree

# url = "http://example.com"
# page = urlopen(url)
# html_code = page.read().decode('utf-8')

# tree = etree.HTML(html_code)
# elem = tree.xpath("/html/body/div/p[1]")[0]
# temp = elem.text
# print(temp)



# url = "https://youtu.be/ZdMC7H6KDtU?si=Nk09lMSLAUVPVcMn"
# page = urlopen(url)
# html_code = page.read().decode('utf-8')

# tree = etree.HTML(html_code)
# elem = tree.xpath("/html/body/ytd-app/div[1]/ytd-page-manager")	
# print(elem)



# parser = etree.HTMLParser()
# html_root = etree.fromstring(html_code, parser)

# result = etree.tostring(html_root, pretty_print=True, method="html")

# print(html_code)
# print('\n\n\n')
# print(html_root)
# print('\n\n\n')
# print(result)