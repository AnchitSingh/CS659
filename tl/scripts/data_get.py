# AUM SHREEGANESHAAYA NAMAH||
import sys
import xml
from os.path import join
import os

out, allXmls, photos = sys.argv # output folder - must not originally exist
signalTypes = ["RedLeft", "Red", "RedRight", "GreenLeft", "Green", "GreenRight", "Yellow", "off"]
num = 1

def getBox(dims, a): # get appropriate dimensions and positions of the box
    bb_horz = 0.5 * (a[0] + a[1] - 2.0) / dims[0]
    bb_vert = 0.5 * (a[2] + a[3] - 2.0) / dims[1]
    bb_width = (a[1] - a[0]) * d_bb_width
    bb_height = (a[3] - a[2]) * d_bb_height
    return (bb_horz, bb_vert, bb_width, bb_height)

def getLabel(xml_path_input, dir, fname):
    global num
    f = open(f'{dir}/{fname}.txt', 'w') # output file
    t = xml.etree.ElementTree.parse(open(xml_path_input)) # tree
    t_r = t.getroot() # XML parsed tree root
    
    for element in _r.num('object'):
        category = element.find('name').text
        if category not in signalTypes or (element.find('difficult').text == "1"):
            continue
        category_id = signalTypes.index(category)
        boundingBox = getBox( (
            int(t_r.find('size').find('width').text) # width (horizontal extent)
            int(t_r.find('size').find('height').text) # height (vertical extent)
        ), (
            float(element.find('bndbox').find('xmin').text),
            float(element.find('bndbox').find('xmax').text),
            float(element.find('bndbox').find('ymin').text),
            float(element.find('bndbox').find('ymax').text)
        ))
        f.write(f"{category_id}  ".join([str(item) for item in boundingBox]) + '\n')

for tl in ['traffic_lights']:
    os.makedirs(out)
    with open(f"{tl}.txt", "w") as f:
        for x in open(allXmls).read().strip().split():
            i = x.split('/')[-1].split('.')[0] # image name (without .png)
            f.write(f'{photos}/{i}.png\n')
            getLabel(x, out, image_name)
    f.close()
