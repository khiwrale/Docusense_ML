#!/usr/bin/env python
# coding: utf-8

# Importing Dependencies

from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileMerger
import os

class Image_Convertor:
    
    def pdf_2_jpg():
        # Setting the I/P & O/P file paths
        IP_path = "C:/Docusense-ML/src/data/PDF/" 

        OP_path1 = "C:/Docusense-ML/src/data/output/" #jpg path

        pdfname = IP_path + input('Enter PDF name with extension: ')

        # Counting the number of pages in the pdf and converting the pages into image
        images = convert_from_path(pdfname)
        i = 1
        length = len(images)

        print("Number of pages in PDF="+str(length))

        for image in images:
            image.save(OP_path1 + str(i) + '.jpg', 'JPEG')
            i = i + 1
        
    def pdf_2_png():
        # Setting the I/P & O/P file paths
        IP_path = "C:/Docusense-ML/src/data/PDF/" 

        OP_path2 = "C:/Docusense-ML/src/data/output/" #png path

        pdfname = IP_path + input('Enter PDF name with extension: ')

        # Counting the number of pages in the pdf and converting the pages into image
        images = convert_from_path(pdfname)
        i = 1
        length = len(images)

        print("Number of pages in PDF="+str(length))

        for image in images:
            image.save(OP_path2 + str(i) + '.png', 'PNG')
            i = i + 1
    
    def png_2_pdf():
        
        IP_path2 = "C:/Docusense-ML/src/data/PDF/"
        OP_path = "C:/Docusense-ML/src/data/output/"
        
        img_list = [os.path.join(IP_path2, file)
                for file in os.listdir(IP_path2)
                if file.endswith('.png')]

        for i,path in enumerate(img_list):
            image_1 = Image.open(path)
            im_1 = image_1.convert('RGB')
            im_1.save(OP_path+str(i)+'.pdf')    
        
    def jpg_2_pdf():
        IP_path1 = "C:/Docusense-ML/src/data/PDF/"
        OP_path = "C:/Docusense-ML/src/data/output/"

        img_list = [os.path.join(IP_path1, file)
                for file in os.listdir(IP_path1)
                if file.endswith('.jpg')]

        for i,path in enumerate(img_list):
            new_image_1 = Image.open(path)
            new_im_1 = new_image_1.convert('RGB')
            new_im_1.save(OP_path+str(i)+'.pdf')


Image_Convertor.pdf_2_jpg()

Image_Convertor.jpg_2_pdf()

# fuction to merge all pdfs into a single pdf in a given folder
def merge_pdf():

    pdf_list = [os.path.join(OP_path, file)
            for file in os.listdir(OP_path)
            if file.endswith('.pdf')]

    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(OP_path+"result.pdf")
    merger.close()

from pathlib import Path
 
path = Path("C:/Docusense-ML/src/data/PDF/")
files_in_path = path.iterdir()
for item in files_in_path:
    if item.is_file():
        print(item.name)
        

#Image Metadata Extraction

import os
from PIL import Image
from PIL.ExifTags import TAGS

IP_path = "C:/Docusense-ML/src/data/PDF/"

img_list = [os.path.join(IP_path, file)
        for file in os.listdir(IP_path)
        if file.endswith('.jpg')]

for i in img_list:
    image = Image.open(i)
    
    # extracting the exif metadata
    exifdata = image.getexif()
    
# looping through all the tags present in exifdata
for tagid in exifdata:
    
    # getting the tag name instead of tag id
    tagname = TAGS.get(tagid, tagid)

    # passing the tagid to get its respective value
    value = exifdata.get(tagid)

    # printing the final result
    print(f"{tagname:25}: {value}")


import PyPDF2

filename = "C:/Docusense-ML/src/data/PDF/0.pdf"

pdfFile = PyPDF2.PdfFileReader(filename,'rb')
data = pdfFile.getDocumentInfo()

print("----Metadata of the file----")

for metadata in data:
    print(metadata+ ":" +data[metadata])