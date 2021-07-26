import zstandard

filePath = 'C:\\onedrive\\OneDrive - University of Florida\\Desktop\\Lab\\Yahoo_QA\\megawarc-zst-original\\yahooanswers_20210423210648_f6a9de36\\20210423210648_f6a9de36'
fileName = 'yahooanswers-00aa1481a0b1ca540f6494d361d96d44b3204365-20210421-161140.yahooanswers.1618939290.warc.zst'
input_path = filePath + '\\' + fileName
output_path = filePath + "yahooanswers-00aa1481a0b1ca540f6494d361d96d44b3204365-20210421-161140"
dictPath = filePath + '\\' + 'archiveteam_yahooanswers_dictionary_1618939290.zstdict'
with open(dictPath, 'rb') as dictfh, open(input_path, 'rb') as ifh, open(output_path, 'wb') as ofh:
    dctx = zstandard.ZstdDecompressor(dict_data=dictfh)
    dctx.copy_stream(ifh, ofh)

