# AUM SHRREEGANESHAAYA NAMAH||
import requests

server = "http://192.168.1.39:5000"

def getLabel(imgPath):
	r = requests.post( f"{server}/upload", files = { 'media' : open(imgPath, 'rb') } ).text.split("|")
	return r
