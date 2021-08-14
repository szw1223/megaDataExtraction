from warcio.archiveiterator import ArchiveIterator
import os
import json
from bs4 import BeautifulSoup


def targetFilter(path):

    summaryCategory = {}
    # use os.scandir to scan each file
    scadndir = os.scandir(path)

    # open each file from 2400
    for name in scadndir:
        fileName = path + name.name
        saveID = name.name.split('-')[1]
        print(name)
        with open(fileName, 'rb') as stream:

            # iterate items in each file
            for record in ArchiveIterator(stream):
                byteToStr = str(record.content_stream().read())
                # if resource type is response, read the content
                if '<!DOCTYPE html>' in byteToStr:

                    soup = BeautifulSoup(byteToStr, 'html.parser')

                    jsonList = soup.find_all(type="application/ld+json")

                    try:
                        strJson0 = str(jsonList[0])

                        indexOf = strJson0.index('>') + 1
                        strJson0 = strJson0[indexOf: -9]
                        JsonDict0 = json.loads(strJson0)
                        listCategory = JsonDict0['itemListElement']
                        print(listCategory)
                        # len_categories = len(JsonDict0['itemListElement'])

                        if listCategory[0]['name'] not in summaryCategory.keys():
                            summaryCategory[listCategory[0]['name']] = {}
                        if listCategory[1]['name'] not in summaryCategory[listCategory[0]['name']].keys():
                            summaryCategory[listCategory[0]['name']][listCategory[1]['name']] = []
                            summaryCategory[listCategory[0]['name']][listCategory[1]['name']].append(listCategory[2]['name'])
                        else:
                            if listCategory[2]['name'] not in summaryCategory[listCategory[0]['name']][listCategory[1]['name']]:
                                summaryCategory[listCategory[0]['name']][listCategory[1]['name']].append(
                                    listCategory[2]['name'])
                    except:
                        print('nima')
    print(summaryCategory)
    with open('summaryCategory.json', 'w') as outfile:
        json.dump(summaryCategory, outfile)

if __name__ == "__main__":
    targetPath = 'C:\\onedrive\\OneDrive - University of Florida\\Desktop\\Lab\\Yahoo_QA\\4000warcs\\'


    targetFilter(targetPath)