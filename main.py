import os

def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".zst"):
                os.remove(os.path.join(root,name))
    print ("Delete File: " + os.path.join(root, name))

# test
if __name__ == "__main__":
    filePath = '/home/zheweisong/PycharmProjects/megaDealing'
    dirList = os.listdir(filePath)
    dirList.sort()
    dictName = dirList[1]
    lenDir = len(dirList)
    print(dictName)
    for i in dirList[4:]:
        commandLine = 'unzstd -D ' + dictName + ' ' + i
        os.system(commandLine)

    del_files(filePath)
