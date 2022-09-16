import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


class Image_Preprocess():
    def __init__(self,input_path,output_path):
        self.input_path = input_path
        self.output_path = output_path
        
    def png_preprocess(self):
        files = os.listdir(self.input_path)
        print(files)
        for file in files:
            os.makedirs(f'{self.output_path}/{file}')
            png_list = [os.path.join(f'{self.input_path}\\{file}', f)
                    for f in os.listdir(f'{self.input_path}\\{file}')
                    if f.endswith('.png')]
            for img in png_list:
                img = img.replace('\\','/')
                name_extension = img.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                ip_image = cv2.imread(img)
                inv_img = cv2.bitwise_not(ip_image)
                gray_img = cv2.cvtColor(inv_img, cv2.COLOR_BGR2GRAY ) #grayscale
                thresh, bw_img = cv2.threshold(gray_img, 128,255, cv2.THRESH_BINARY)  #adjusting_black_white
                kernel = np.ones((1,1), np.uint8)
                image = cv2.dilate(bw_img, kernel, iterations = 1)
                imaged = cv2.erode(image, kernel, iterations = 1)
                imagem = cv2.morphologyEx(imaged, cv2.MORPH_CLOSE, kernel)
                imageo = cv2.medianBlur(imagem, 3)
                erod_img = cv2.erode(imageo, kernel, iterations = 1)
                cv2.imwrite(f'{self.output_path}/{file}/{name}.png',erod_img)
        return "Preprocess Completed"

    def jpg_preprocess(self):
        files = os.listdir(self.input_path)
        for file in files:
            os.makedirs(f'{self.output_path}/{file}')
            png_list = [os.path.join(f'{self.input_path}\\{file}', f)
                    for f in os.listdir(f'{self.input_path}\\{file}')
                    if f.endswith('.jpg')]
            for img in png_list:
                img = img.replace('\\','/')
                name_extension = img.rsplit("/")[-1]
                name = name_extension.rsplit('.')[0]
                print(img)
                ip_image = cv2.imread(img)
                inv_img = cv2.bitwise_not(ip_image)
                gray_img = cv2.cvtColor(inv_img, cv2.COLOR_BGR2GRAY ) #grayscale
                thresh, bw_img = cv2.threshold(gray_img, 128,255, cv2.THRESH_BINARY)  #adjusting_black_white
                kernel = np.ones((1,1), np.uint8)
                image = cv2.dilate(bw_img, kernel, iterations = 1)
                imaged = cv2.erode(image, kernel, iterations = 1)
                imagem = cv2.morphologyEx(imaged, cv2.MORPH_CLOSE, kernel)
                imageo = cv2.medianBlur(imagem, 3)
                erod_img = cv2.erode(imageo, kernel, iterations = 1)
                cv2.imwrite(f'{self.output_path}/{file}/{name}.jpg',erod_img)
        return "Preprocess Completed"

# Image_Preprocess('C:\Docusense-ML\src\data\output\pdf_to_png','C:\Docusense-ML\src\data\output\preprocess_images').png_preprocess()