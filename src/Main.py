from flask import Flask, jsonify, request, redirect, url_for
from flask_restful import Api, Resource, reqparse
from source.file_handler import Pdf2Img_convertor, Img2pdf_convertor
from source.Preprocessing import Image_Preprocess
from source.Tesseract_Module import TextExraction
from Pdftopng import Convert
from Preprocessing import Preprocess
from Tesseract import Tesseract
import requests

import werkzeug

app = Flask(__name__)
api = Api(app)

argument_parser = reqparse.RequestParser()
argument_parser.add_argument("input_path", type=str, location='form')
argument_parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files') 


IP_PATH = "C:\Docusense-ML\src\data\PDF"
OP_PATH = "C:\Docusense-ML\src\data\output\pdf_to_png"
OP_PATH_png = "C:\Docusense-ML\src\data\output\preprocess_images"
OP_PATH_tess = "C:\Docusense-ML\src\data\output\preprocess_to_text"

@app.route('/user',methods=['POST'])
def checking():
    args = argument_parser.parse_args()
    Ip_pdf = args['file']
    # input_path = args['input_path']
    PdfConverter = Pdf2Img_convertor(IP_PATH,OP_PATH,pdf_file=Ip_pdf)
    output_png = PdfConverter.pdf_2_png()
    ImagePreprocess = Image_Preprocess(OP_PATH,OP_PATH_png)
    output_png = ImagePreprocess.png_preprocess()
    Imagetxt = TextExraction(OP_PATH_png,OP_PATH_tess)
    output_txt = Imagetxt.png_to_text()
    return f'Text Extraction Completed !'



if __name__ == "__main__":
    app.run(debug=True,port=5900)