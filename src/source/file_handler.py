#!/usr/bin/env python
# coding: utf-8

# Importing Dependencies for file handling
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader

import os
import os.path

# Importing Dependencies for Metadata Extraction
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


# #### PDF to Image Coversion Class

class Pdf2Img_convertor:
    
    def __init__ (self, input_pdf_path, output_img_path,pdf_file):
        self.input_pdf_path = input_pdf_path
        self.output_img_path = output_img_path
        self.pdf_file = pdf_file
          
    
    def pdf_2_png(self):
        if self.pdf_file == None:
            self.output_img_path = self.output_img_path.replace("\\","/")
            pdf_list = [os.path.join(self.input_pdf_path, f)
                for f in os.listdir(self.input_pdf_path)
                if f.endswith('.pdf')]
            for file in pdf_list:
                file = file.replace('\\','/')
                print('we are checking file path',file)
                images = convert_from_path(pdf_path= file, poppler_path=r'C:\Program Files\poppler-0.68.0\bin',dpi=500,fmt='png')
                name_extension = file.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                os.makedirs(f'{self.output_img_path}/{name}')
                for i ,page in enumerate(images):
                    page.save(f'{self.output_img_path}/{name}/{name}_{i+1}.png','PNG')

        else:
            self.output_img_path = self.output_img_path.replace("\\","/")
            pdf_list = [os.path.join(self.input_pdf_path, f)
                for f in os.listdir(self.input_pdf_path)
                if f.endswith('.pdf')]
            pdf_list.append(self.pdf_file)
            for file in pdf_list:
                file = file.replace('\\','/')
                images = convert_from_path(pdf_path= file, poppler_path=r'C:\Program Files\poppler-0.68.0\bin',dpi=500,fmt='png')
                name_extension = file.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                os.makedirs(f'{self.output_img_path}/{name}')
                for i ,page in enumerate(images):
                    page.save(f'{self.output_img_path}/{name}/{name}_{i+1}.png','PNG')
            
        return 'Pdf converted into PNG'
    
    
    def pdf_2_jpg(self):
        if self.pdf_file != None:
            self.output_img_path = self.output_img_path.replace("\\","/")
            pdf_list = [os.path.join(self.input_pdf_path, f)
                for f in os.listdir(self.input_pdf_path)
                if f.endswith('.pdf')]
            for file in pdf_list:
                file = file.replace('\\','/')
                images = convert_from_path(pdf_path= file, poppler_path=r'C:\Program Files\poppler-0.68.0\bin',dpi=500,fmt='png')
                name_extension = file.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                for i ,page in enumerate(images):
                    page.save(f'{self.output_img_path}/{name}_{i+1}.jpg','Jpeg')
        return 'Pdf converted into JPG'
#pdf2Img_convertor(IP_file)

# ip_path = "C:\Docusense-ML\src\data\PDF"
# op_path = "C:\Docusense-ML\src\data\output"

# convertor = Pdf2Img_convertor(ip_path, op_path,"C:\Docusense-ML\src\data\PDF\1.pdf")

# convertor.pdf_2_png()

# #### Images to PDF Coversion Class

class Img2pdf_convertor:
    
        
    def __init__ (self, path, path1):
        self.path = path
        self.path1 = path1
        
    #PNG to PDF Conversion Function
    def png_2_pdf(self):
                
        file_list = [os.path.join(self.path, f) 
                     for f in os.listdir(self.path) 
                     if os.path.isfile(os.path.join(self.path, f))]
        
        img_list = [os.path.join(self.path, file)
                for file in os.listdir(self.path)
                if file.endswith('.png')]
        
        print("Number of Images="+str(len(img_list)))

        for i,path in enumerate(img_list):
            image_1 = Image.open(path)
            im_1 = image_1.convert('RGB')
            im_1.save(self.path1+str(i)+'.pdf') 
        
    #JPEG to PDF Conversion Function    
    def jpg_2_pdf(self):

        img_list = [os.path.join(self.path, file)
                for file in os.listdir(self.path)
                if file.endswith('.jpg')]
        
        print("Number of Images="+str(len(img_list)))

        for i,path in enumerate(img_list):
            new_image_1 = Image.open(path)
            new_im_1 = new_image_1.convert('RGB')
            new_im_1.save(self.path1+str(i)+'.pdf')
    
    # fuction to merge all pdfs into a single pdf in a given folder
    def merge_pdf():

        pdf_list = [os.path.join(self.path1, file)
                for file in os.listdir(self.path1)
                if file.endswith('.pdf')]

        merger = PdfFileMerger()

        for pdf in pdf_list:
            
            if not os.path.exists('my_folder'):
                os.makedirs('my_folder')
            merger.append(pdf)

        merger.write('my_folder/result.pdf')
        merger.close()
        
        # deleting extra pdfs
        for j in range (len(pdf_list)):
            os.remove(self.path1+str(j)+'.pdf')



# ip_path = "C:\Docusense-ML\src\data\PDF"
# op_path = r'C:/Tuteck/output/'

# convertor = Img2pdf_convertor(ip_path, op_path)
# convertor.png_2_pdf()


# #### MetaData Extraction Class

# class Metadata_extraction:
    
#     def __init__ (self, path):
#         self.path = path

#      # Size Conversion
#     def convert_bytes(self, size):

#         for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
#             if size < 1024.0:
#                 return "%3.1f %s" % (size, x)
#             size /= 1024.0
   
        
    
#     def meta_extractor(self):

        
#         file_list = [os.path.join(self.path, f) 
#                      for f in os.listdir(self.path) 
#                      if os.path.isfile(os.path.join(self.path, f))]
        
#         for file in file_list:
#             if file.endswith('.pdf'):
#                 self.pdf_metadata(file)
                
#                 #self.convert_bytes(os.path.getsize(file))
#                 y = convert_bytes(os.path.getsize(file))
#                 print('File size: ' + y)
                
#                 print('\n')
#             else:
#                 self.image_metadata(file)
#                 #self.convert_bytes(os.path.getsize(file))
                
#                 y = convert_bytes(os.path.getsize(file))
#                 print('File size: ' + y)
                
#                 print('\n')
            
            
#     # Image Metadata Extraction
#     def image_metadata(self, filename):
        
#       #  for filename in img_list:
#         parser = createParser(filename)
#         metadata = extractMetadata(parser)
#         metadata = metadata.exportPlaintext()

#         print('Metadata of Image: ' + filename)
        
#         for fields in metadata:
#             print(fields)
                
#     # PDF Metadata Extraction
#     def pdf_metadata(self, filename):

#         pdf = PdfFileReader(filename)
#         info = pdf.getDocumentInfo()
        
#         print('Metadata of Document: ' + filename)
        
#         for fields in info:
#             print(fields+ ":" + str(info[fields]))  
        

IP_file = "C:\Docusense-ML\src\data\PDF"
# meta = Metadata_extraction(IP_file)
# MetaData = meta.meta_extractor()
# MetaData