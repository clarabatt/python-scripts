from wand.image import Image
import os
import re

SourceFolder="/mnt/c/Users/Owner/Downloads/Print"
TargetFolder="/mnt/c/Users/Owner/Downloads/Print/jpg"

sum = 0

for file in os.listdir(SourceFolder):
    if (re.search('heic', file)):
        sum+=1
        print(f"{sum} files")
        SourceFile=SourceFolder + "/" + file
        TargetFile=TargetFolder + "/" + file.replace(".heic",".jpg")

        img=Image(filename=SourceFile)
        img.format='jpg'
        img.save(filename=TargetFile)
        img.close()