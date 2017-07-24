import xml.etree.ElementTree as et
import re
import os
from PIL import Image, ImageFont, ImageDraw

path = os.getcwd()


reImgFile = re.compile("(.*).png")
for file in os.listdir("."):
	name = reImgFile.match(file)
	if name != None:
		imgName = name.group(1)
		print(imgName)
		imgFile = Image.open(name.group(0))
		file = open(imgName + r".plist", "rb")

		stateFile = 1
		statePos = 2
		stateRotate = 3

		imgFile = Image.open("att_pin.png")
		file = open("att_pin.plist", "rb")
		reName = re.compile(r".*<key>games/.*/(.*?)/(.*?.png)</key>.*")
		rePos = re.compile(r".*<string>{{(\d+),(\d+)},{(\d+),(\d+)}}</string>.*")
		reRotate = re.compile(r".*(<false/>)|(<true/>).*")
		reFalse = re.compile(r".*<false />.*")
		reTrue = re.compile(r".*<true />.*")
		curState = stateFile
		filePath = ""
		fileName = ""
		x = 0
		y = 0
		w = 0
		h = 0
		for line in file.readlines():
			line = line.decode("utf-8")
			if curState == stateFile:
				result = reName.match(line)
				if result != None:
					filePath = result.group(1)
					fileName = result.group(2)
					curState = statePos
					print(filePath)
					print(fileName)
			elif curState == statePos:
				posResult = rePos.match(line)
				# print(line)
				if posResult != None:
					x = int(posResult.group(1))
					y = int(posResult.group(2))
					w = int(posResult.group(3))
					h = int(posResult.group(4))
					curState = stateRotate
					
			elif curState == stateRotate:
				notRotate = reFalse.match(line)
				isRotate = reTrue.match(line)
				if notRotate != None:
					box = (x, y, x + w, y + h)
					print(box)
					imgFrame = imgFile.crop(box)
					if not os.path.exists(path + "\\" + filePath):
						os.mkdir(path + "\\" + filePath)			
					fullFilePath = path + "\\" + filePath + "\\" + fileName
					# print(fullFilePath)
					imgFrame.save(fullFilePath)
					curState = stateFile
				elif isRotate != None:
					box = (x, y, x + h, y + w)
					print(box)
					imgFrame = imgFile.crop(box)
					if not os.path.exists(path + "\\" + filePath):
						os.mkdir(path + "\\" + filePath)			
					fullFilePath = path + "\\" + filePath + "\\" + fileName
					# print(fullFilePath)
					imgFrame.save(fullFilePath)
					curState = stateFile

		imgFile.close()
		file.close()

# reRotate = re.compile(r"(.*<false />.*)|(.*<true />.*)")
# line = r"				<true />"
# result = reRotate.match(line)
# print(result)