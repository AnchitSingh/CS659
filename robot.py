#! /usr/bin/python3
# AUM SHREEGANESHAAYA NAMAH||
import sys
from os import path, mkdir
from shutil import rmtree
import requests
from gpiozero import Robot
from picamera import PiCamera
from time import sleep

rb = Robot(left=(9, 10), right=(7, 8))
cam = PiCamera()
server = "http://192.168.1.39:5000"

if (len(sys.argv) < 2):
	print("Please enter path to store images.")
	exit(-1)

imgPath = sys.argv[1]

if not path.isdir(imgPath):
	print(f"\"{imgPath}\" is not a valid path.")
	exit(-2)

print(f"Cleansing {imgPath} ...")
rmtree(imgPath)
mkdir(imgPath)

totalImg = 0

rb.forward()

while True:
	print(f"Capturing {totalImg}.png")
	savePath = path.join(imgPath, f"{totalImg}.png")
	cam.capture(savePath)
	resp = requests.post( f"{server}/upload", files={ 'media' : open(savePath, "rb") } ).text.split("|")
	print(resp)
	if resp == "Green":
		rb.stop()
	totalImg += 1




