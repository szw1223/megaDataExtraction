from warcio.archiveiterator import ArchiveIterator
import os
import json

data = {}

# use os.scandir to scan each file
scadndir=os.scandir('C:\\programming\\Python\\Project\\megaDataExtraction\\2000warcs\\')
qIdList = []
health = []

countInRepns = 0
countInHealth = 0

# open each file from 660
for name in scadndir:
    fileName = 'C:\\programming\\Python\\Project\\megaDataExtraction\\2000warcs\\' + name.name

    with open(fileName, 'rb') as stream:

        # iterate items in each file
        for record in ArchiveIterator(stream):

            # if resource type is response, read the content
            if record.rec_type == 'response' and int(record.rec_headers.get_header('Content-Length')) > 50000:

                countInRepns += 1
                byteToStr = str(record.content_stream().read(), 'utf-8')
                if '<a href="https://answers.yahoo.com/dir/index?sid=396545018">' in byteToStr:

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

