import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime
from tkinter import filedialog
import os
import os.path
import json
import matplotlib
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class TextExraction():
    def __init__ (self, input_png_path , output_txt_path):
        self.input_png_path = input_png_path
        self.output_txt_path = output_txt_path
        # self.png_file = png_file
        
    def png_to_text(self):
        self.output_txt_path = self.output_txt_path.replace("\\","/")
        self.input_png_path = self.input_png_path.replace('\\','/')
        files = os.listdir(self.input_png_path)
        for file in files:
            # print('inputfile',file)
            os.makedirs(f'{self.output_txt_path}/{file}')
            png_list = [os.path.join(f'{self.input_png_path}/{file}', f)
                for f in os.listdir(f'{self.input_png_path}/{file}')
                if f.endswith('.png')]
            print(png_list)
            for png in png_list:
                png = png.replace('\\','/')
                name_extension = png.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                # print(name_extension)
                text = pytesseract.image_to_string(png) 
                with open(f"{self.output_txt_path}/{file}/{name}.txt", "w") as text_file:
                    text_file.write(text)

        return 'Png to text Extracted'
        
    
    def jpg_to_text(self):
        self.output_txt_path = self.output_txt_path.replace("\\","/")
        self.input_png_path = self.input_png_path.replace('\\','/')
        files = os.listdir(self.input_png_path)
        for file in files:
            # print('inputfile',file)
            os.makedirs(f'{self.output_txt_path}/{file}')
            png_list = [os.path.join(f'{self.input_png_path}/{file}', f)
                for f in os.listdir(f'{self.input_png_path}/{file}')
                if f.endswith('.jpg')]
            print(png_list)
            for png in png_list:
                png = png.replace('\\','/')
                name_extension = png.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                # print(name_extension)
                text = pytesseract.image_to_string(png) 
                with open(f"{self.output_txt_path}/{file}/{name}.txt", "w") as text_file:
                    text_file.write(text)

        return 'Jpg to text Extracted'

# TextExraction('C:\Docusense-ML\src\data\output\preprocess_images','C:\Docusense-ML\src\data\output\png_to_text','axis1.png').png_to_text()