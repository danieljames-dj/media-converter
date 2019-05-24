import os
from os.path import splitext
import re

fileListString = input("Drag and drop the file you want to convert: ")
fileList = re.split('(?<!\\\\)\\s+', fileListString.strip())
for file in fileList:
	print(file)
	filename,ext = splitext(file)
	print(filename)
	print(ext)
	os.system("ffmpeg -i " + filename + ext + " " + filename + ".mp3")