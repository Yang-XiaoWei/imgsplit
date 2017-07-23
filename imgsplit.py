import xml.etree.ElementTree as et
import re
import os
from PIL import Image, ImageFont, ImageDraw

path = os.getcwd()


imgFile = Image.open("att_pin.png")

file = open("att_pin.plist", "rb")
reName = re.compile(r".*<key>games/.*/(.*?)/(.*?.png)</key>.*")
rePos = re.compile(r".*<string>{{(\d+),(\d+)},{(\d+),(\d+)}}</string>.*")
nowIsName = True
filePath = ""
fileName = ""
for line in file.readlines():
	line = line.decode("utf-8")
	if nowIsName:
		result = reName.match(line)
		if result != None:
			filePath = result.group(1)
			fileName = result.group(2)
			nowIsName = False
			print(filePath)
			print(fileName)
	if not nowIsName:
		posResult = rePos.match(line)
		# print(line)
		if posResult != None:
			x = int(posResult.group(1))
			y = int(posResult.group(2))
			w = int(posResult.group(3))
			h = int(posResult.group(4))
			box = (x, y, x + w, y + h)
			print(box)
			imgFrame = imgFile.crop(box)
			if not os.path.exists(path + "\\" + filePath):
				os.mkdir(path + "\\" + filePath)			
			fullFilePath = path + "\\" + filePath + "\\" + fileName
			# print(fullFilePath)
			imgFrame.save(fullFilePath)
			nowIsName = True

file.close()
