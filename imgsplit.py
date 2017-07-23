import xml.etree.ElementTree as et
import re
import os
from PIL import Image, ImageFont, ImageDraw

# path = os.getcwd()

# stateFile = 1
# statePos = 2
# stateRotate = 3

# imgFile = Image.open("att_pin.png")

# file = open("att_pin.plist", "rb")
# reName = re.compile(r".*<key>games/.*/(.*?)/(.*?.png)</key>.*")
# rePos = re.compile(r".*<string>{{(\d+),(\d+)},{(\d+),(\d+)}}</string>.*")
# reRotate = re.compile(r".*(<false/>)|(<true/>).*")
# curState = stateFile
# filePath = ""
# fileName = ""
# x = 0
# y = 0
# w = 0
# h = 0
# for line in file.readlines():
# 	line = line.decode("utf-8")
# 	if curState == stateFile:
# 		result = reName.match(line)
# 		if result != None:
# 			filePath = result.group(1)
# 			fileName = result.group(2)
# 			curState = statePos
# 			print(filePath)
# 			print(fileName)
# 	if curState == statePos:
# 		posResult = rePos.match(line)
# 		# print(line)
# 		if posResult != None:
# 			x = int(posResult.group(1))
# 			y = int(posResult.group(2))
# 			w = int(posResult.group(3))
# 			h = int(posResult.group(4))
# 			box = (x, y, x + w, y + h)
# 			print(box)
# 			imgFrame = imgFile.crop(box)
# 			if not os.path.exists(path + "\\" + filePath):
# 				os.mkdir(path + "\\" + filePath)			
# 			fullFilePath = path + "\\" + filePath + "\\" + fileName
# 			# print(fullFilePath)
# 			imgFrame.save(fullFilePath)
# 			curState = stateRotate

# 	if curState == stateRotate:


# file.close()

reRotate = re.compile(r".*(<false/>)|(<true />).*")
line = r"				<true />"
result = reRotate.match(line)
print(result)