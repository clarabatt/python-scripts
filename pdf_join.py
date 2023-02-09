from PyPDF3 import PdfFileMerger
import os
import re

SourceFolder="/mnt/c/Users/Owner/Downloads/pdfs"

merger = PdfFileMerger()

index = 0
documentsList = []

for file in os.listdir(SourceFolder):
    if (re.search('pdf', file)):
        documentsList.append(open(fr"{file}", "rb"))
        index += 1
        print(f"{sum} document{sum and 's'}")

for doc in documentsList:
    merger.append(doc)

output = open(f"{SourceFolder}/documents-output.pdf", "wb")
merger.write(output)
