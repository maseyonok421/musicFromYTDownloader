from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle ( url ):
	site = urlopen(url)
	page = BeautifulSoup(site, 'html.parser')
	return page.find('title').string

# url  = "https://example.com"
url  = "https://youtu.be/1COE-eZo6gg?si=HZp3Ep9Zkv0WOTKb"
print(getTitle(url))
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