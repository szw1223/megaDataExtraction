import pandas as pd
import os


def statisticsOfCollection(filePath, readSheetName, saveSheetName, begin, end):
    # read file
    excelData = pd.DataFrame(pd.read_excel(filePath, sheet_name=readSheetName))
    listYear = list(range(begin, end))
    dictCollection = {}

    # loop the year list (each year)
    for i in listYear:
        oneYearCllct = excelData[i].astype(str)

        # loop the collection in each year
        for j in range(len(oneYearCllct)):
            print(oneYearCllct[j])
            if oneYearCllct[j] in dictCollection.keys():
                dictCollection[oneYearCllct[j]] += 1
            else:
                dictCollection[oneYearCllct[j]] = 1

    # sort dictionary by frequency
    dictCollection = sorted(dictCollection.items(), key=lambda x: x[1], reverse=True)[1:]

    # save into excel
    listKey = []
    listValue = []
    for key, value in dictCollection:
        listKey.append(key)
        listValue.append(value)

    dicExcel = {}
    dicExcel['collection'] = listKey
    dicExcel['frequency'] = listValue

    df = pd.DataFrame(dicExcel)
    df.to_excel('sortCollection.xlsx', index=False, sheet_name=saveSheetName)
    # print(listValue)
    # print(dictCollection)
    # print(len(dictCollection) - 1)

if __name__ == '__main__':
    filePath = os.path.abspath('listOfCollection.xlsx')
    statisticsOfCollection(filePath, 'yearList', 'sortByFrequent', 2006, 2021)