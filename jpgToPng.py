from PIL import Image, ImageFilter
import sys
import os 

# input:
# jpgToPng.py .\Pictures .\new

# grab first and second argument -> Use sys.argv
# img_files = os.listdir(sys.argv[1])
# new_files = sys.argv[2]
img_files = os.listdir(r".\Pictures")
new_files = r".\new"
# check if \new folder exists, if not, create the folder
print(os.path.exists(new_files))

# loop through the pictures file
# convert images to png
# save to the new folder

# print(os.name)
print(os.getcwd())

