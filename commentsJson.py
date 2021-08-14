from warcio.archiveiterator import ArchiveIterator
import os
import json
from bs4 import BeautifulSoup


def targetFilter(targetStr, path, output_folder):

    # use os.scandir to scan each file
    scadndir = os.scandir(path)

    qIdList = []
    health = []
    comments = []

    countInRepns = 0
    countInHealth = 0
    countComment = 0

    # open each file from 2400
    for name in scadndir:
        fileName = path + name.name
        saveID = name.name.split('-')[1]
        print(saveID)
        with open(fileName, 'rb') as stream:

            # iterate items in each file
            for record in ArchiveIterator(stream):
                byteToStr = str(record.content_stream().read(), 'utf-8')
                # if resource type is response, read the content
                if '<!DOCTYPE html>' in byteToStr:

                    countInRepns += 1

                    if targetStr in byteToStr:

                        soup = BeautifulSoup(byteToStr, 'html.parser')

                        jsonList = soup.find_all(type="application/ld+json")

                        strJson0 = str(jsonList[0])
                        indexOf = strJson0.index('>') + 1

                        strJson1 = str(jsonList[1])[indexOf: -9]
                        JsonDict1 = json.loads(strJson1, strict=False)
                        if 'comment' in strJson1:

                            countComment += 1
                            comments.append(strJson1)

                        print(strJson1)
                        print("!!!!!!!!!!!!!!JsonDict")
                        print(JsonDict1)

                        print(record.rec_headers.get_header('WARC-Target-URI'))
                        health.append(record.rec_headers.get_header('WARC-Target-URI'))
                        print(record.rec_headers.get_header('X-Wget-AT-Project-Item-Name'))
                        qIdList.append(record.rec_headers.get_header('X-Wget-AT-Project-Item-Name'))
                        countInHealth += 1
                        print("exist")
                        print(fileName)
                    else:
                        print('None')

    print(countInRepns)
    print(countInHealth)
    print(countComment)
    print(comments)

if __name__ == "__main__":
    targetPath = 'C:\\Users\\szw12\\Documents\\GitHub\\megaDataExtraction\\2000warcs\\'
    target = '<a href="https://answers.yahoo.com/dir/index?sid=396545018">'
    targetFilter(target, targetPath, 'commentJson')