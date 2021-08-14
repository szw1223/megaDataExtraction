from warcio.archiveiterator import ArchiveIterator
import os
import json
import pandas as pd


def summaryURLs(path, output_folder):

    # use os.scandir to scan each file
    scadndir = os.scandir(path)
    urls = []

    # open each file from 2400
    for name in scadndir:
        fileName = path + name.name
        saveID = name.name.split('-')
        print(saveID)

        with open(fileName, 'rb') as stream:

            # iterate items in each file
            for record in ArchiveIterator(stream):

                url = str(record.rec_headers.get_header('WARC-Target-URI'))
                urls.append(url)
                if 'https://trimurl.im' in url or 'http://www-groups.dcs.st-and.ac.uk' in url:
                    print(saveID)

    dataframe = pd.DataFrame({'url': urls})
    dataframe.to_csv("urls01.csv", index=False, sep=',')


if __name__ == "__main__":
    #targetPath = 'C:\\Users\\szw12\\Documents\\GitHub\\megaDataExtraction\\2000warcs\\'
    targetPath = 'C:\\onedrive\\OneDrive - University of Florida\\Desktop\\Lab\\Yahoo_QA\\4000warcs\\'

    summaryURLs(targetPath, 'output_folder')