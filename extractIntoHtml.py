from warcio.archiveiterator import ArchiveIterator
import os
import json

def targetFilter(targetStr, path, output_folder):

    # use os.scandir to scan each file
    scadndir = os.scandir(path)

    countInRepns = 0
    countInHealth = 0

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
                        countInHealth += 1
                        with open(output_folder + "\\" + saveID + '.html', 'wb') as f:
                            f.write(bytes(byteToStr, encoding="utf8"))
                            f.close()
                    else:
                        print('None')

    print(countInRepns)
    print(countInHealth)

if __name__ == "__main__":
    targetPath = 'C:\\Users\\szw12\\Documents\\GitHub\\megaDataExtraction\\2000warcs\\'
    target = 'comment'
    targetFilter(target, targetPath, 'htmlFolder')