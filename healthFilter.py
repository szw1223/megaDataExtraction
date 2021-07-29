from warcio.archiveiterator import ArchiveIterator
import os
import json
import extractData


def targetFilter(targetStr, path):
    data = {}

    # use os.scandir to scan each file
    scadndir = os.scandir(path)
    qIdList = []
    health = []

    countInRepns = 0
    countInHealth = 0

    # open each file from 2400

    for name in scadndir:
        fileName = path + name.name

        with open(fileName, 'rb') as stream:

            # iterate items in each file
            for record in ArchiveIterator(stream):

                # if resource type is response, read the content
                if record.rec_type == 'response' and int(record.rec_headers.get_header('Content-Length')) > 70000:

                    countInRepns += 1
                    byteToStr = str(record.content_stream().read(), 'utf-8')
                    if targetStr in byteToStr:
                        extractData.extractElements(byteToStr)
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

    with open('healthQuestion.txt', 'w') as outfile:
        json.dump(health, outfile)

    with open('qIdList.txt', 'w') as outfile:
        json.dump(qIdList, outfile)

if __name__ == "__main__":
    targetPath = 'C:\\programming\\Python\\Project\\megaDataExtraction\\2000warcs\\'
    target = '<a href="https://answers.yahoo.com/dir/index?sid=396545018">'
    targetFilter(target, targetPath)