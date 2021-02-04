from PIL import Image, ImageFilter
import sys
import os 

# input:
# jpgToPng.py \Pictures \new

# grab first and second argument -> Use sys.argv
# check if \new folder exists, if not, create the folder

# loop through the pictures file
# convert images to png
# save to the new folder

# img_folder = sys.argv[1]
# new_folder = sys.argv[2]

# print(dir(os))
print()

# print(os.name)
print(os.getcwd())

files = os.listdir(".\Pictures")
print(files)