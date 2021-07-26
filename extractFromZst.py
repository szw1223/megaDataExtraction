import zstd
import zstandard
import os
import zipfile
import pathlib
import shutil

filePath = 'C:\\onedrive\\OneDrive - University of Florida\\Desktop\\Lab\\Yahoo_QA\\megawarc-zst-original\\yahooanswers_20210423210648_f6a9de36\\20210423210648_f6a9de36'
dictPath = 'C:\\onedrive\\OneDrive - University of Florida\\Desktop\\Lab\\Yahoo_QA\\megawarc-zst-original\\yahooanswers_20210423210648_f6a9de36'
listName = []

dictOfList = listName[1].split('.')[2]
dictName = 'archiveteam_yahooanswers_dictionary_' + str(dictOfList) + '.zip'
print(listName[0])
dictNamePath = dictPath + '\\' + dictName
zstdictPath = dictPath + '\\' + 'archiveteam_yahooanswers_dictionary_' + str(dictOfList) + '.zstdict.zst'

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')

def decompress_zstandard_to_folder(input_file):
    input_file = pathlib.Path(input_file)
    with open(input_file, 'rb') as compressed:
        decomp = zstandard.ZstdDecompressor()
        print(input_file.stem, input_file)
        output_path = pathlib.Path(input_file.stem)
        with open(output_path, 'wb') as destination:
            decomp.copy_stream(compressed, destination)

for i, j, k in os.walk(filePath):
    listName = k


unzip_file(dictNamePath, dictPath)

print(dictNamePath)

decompress_zstandard_to_folder(zstdictPath)