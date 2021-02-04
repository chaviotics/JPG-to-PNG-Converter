from PIL import Image, ImageFilter
import sys
import os 

# input:
# jpgToPng.py .\Pictures .\new

# grab first and second argument -> Use sys.argv
img_files = os.listdir(sys.argv[1])
new_files = sys.argv[2]
# img_files = os.listdir(r".\Pictures")
# new_files = r".\new"

# check if \new folder exists, if not, create the folder
if not os.path.exists(new_files): # -> learn how to create folder in python
    os.mkdir(new_files)

# loop through the pictures file
for img in img_files:
    # print(img)
    # convert images to png
    _img = Image.open(".\Pictures"+ "\/" + str(img))
    # save to the new folder
    _img.save(".\/new\/" + str(img)[:-4] + ".png", "png")







