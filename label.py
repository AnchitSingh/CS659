#! /usr/bin/python3
# AUM SHREEGANESHAAYA NAMAH||

from os import system, path, mkdir, remove
import sys
import subprocess

noneTl = { "Red" : 0, "Yellow" : 0, "Green" : 0, "off" : 0, "None" : 100 }
vidTime = 6
weights = 90000
dk = "/home/ishanhmisra/Downloads/659_data/train_rgb/darknet"

def getLabel(imgPath=""):
	try:
		global noneTl
		global dk

		if not path.isfile(imgPath):
			print(f"\"{imgPath}\" is not a file.")
			return ("None", noneTl)

		if path.exists("tmp.mp4"):
			remove("tmp.mp4")

		output = subprocess.check_output(f"ffmpeg -loop 1 -i {imgPath} -c:v libx264  -t {vidTime} -pix_fmt yuv420p tmp.mp4", shell=True).decode('utf-8')

		output = subprocess.check_output(f"{dk}/darknet detector demo {dk}/tl/voc-bosch.data {dk}/tl/test.cfg {dk}/tl/weights/{weights}.weights ./tmp.mp4", shell=True).decode('utf-8')

		lines = output.split('\n')

		labels = { "Red" : [0, 0], "Green" : [0, 0], "Yellow" : [0, 0], "off" : [0, 0] }

		for i in range(len(lines)):
			s = lines[i]
			for label in labels.keys():
				if label in s:
					labels[label][0] += int(s.split(":")[1].strip()[:-1])
					labels[label][1] += 1

		outCome = { }
		isNone = True
		for label in labels.keys():
			if labels[label][1] == 0:
				outCome[label] = 0
			else:
				outCome[label] = labels[label][0] / labels[label][1]
				isNone = False
		if isNone:
			return ("None", noneTl)

		outCome["None"] = 0
		maxLabel = "off"
		for label in outCome.keys():
			if outCome[label] > outCome[maxLabel]:
				maxLabel = label

		return (maxLabel, outCome)
	except:
		return ("None", noneTl)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: <script> [video|image] [path to video/image]")
		exit(-1)

	if sys.argv[1] == "image":
		if len(sys.argv) < 3:
			print("Usage: <script> [video|image] [path to video/image]")
			exit(-1)
		else:
			maxLabel, outCome = getLabel(sys.argv[2])
			print(maxLabel, outCome)
			exit(0)

	if sys.argv[1] == "video":
		inputFile = "" if (len(sys.argv) < 3) else sys.argv[2]
		output = subprocess.check_output(f"{dk}/darknet detector demo {dk}/tl/voc-bosch.data {dk}/tl/test.cfg {dk}/tl/weights/{weights}.weights {inputFile}", shell=True).decode('utf-8')
		print(output)
		exit(0)

	print("Usage: <script> [video|image] [path to video/image]")
	exit(-1)
