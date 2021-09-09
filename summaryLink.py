from bs4 import BeautifulSoup

targetPath = 'C:\\Users\\szw12\\Documents\\GitHub\\megaDataExtraction\\Internet Archive Search_ yahoo answers.html'

with open(targetPath, 'r', encoding='utf-8') as f:
    Soup = BeautifulSoup(f.read(), 'html.parser')
    links = Soup.find_all('div', class_='C234')
    print(type(links))
    print(len(links))
        # .find_all('a')
    print(links)

# https://archive.org/compress/archiveteam_yahooanswers_20210503080031_3cf62ae8/formats=ITEM%20CDX%20INDEX,ITEM%20CDX%20META-INDEX,METADATA,JSON%20GZ,TAR,WEB%20ARCHIVE%20ZST
# https://archive.org/compress/archiveteam_yahooanswers_20210410053534_8ff6af0e/formats=ITEM%20CDX%20INDEX,ITEM%20CDX%20META-INDEX,METADATA,JSON%20GZ,TAR,WEB%20ARCHIVE%20ZST
urlList = []
count = 0
for i in range(len(links)):
    print('----------------------------------------'+ str(i) + '-------------------------------------------')
    link = links[i].find_all('a')
    if len(link) > 0:
        urlPart = links[i].find('div', class_='ttl').get_text()
        urlPartStr = str(urlPart)[46:-14]
        url = 'https://archive.org/compress/archiveteam_yahooanswers_' + urlPartStr + '/formats=ITEM%20CDX%20INDEX,ITEM%20CDX%20META-INDEX,METADATA,JSON%20GZ,TAR,WEB%20ARCHIVE%20ZST'
        urlList.append(url)
        # linkStr = str(link[0])
        # print(linkStr)
        print(urlPartStr)
        count += 1
print(urlList)
print(count)












# url = 'https://archive.org/search.php?query=yahoo+answers&and%5B%5D=mediatype%3A%22web%22&sort=-publicdate&page=2'
#
# driver = webdriver.Chrome(executable_path='C:\\programming\\Python\\anaconda\\setup\\chromedriver-Windows')
#
# driver.get(url)
#
# page = BeautifulSoup(driver.page_source, 'html5lib')
#
#
# js="var q=document.getElementById('id').scrollTop=10000"
# driver.execute_script(js)

# pulldown()






