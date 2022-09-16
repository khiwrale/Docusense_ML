from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from source.file_handler import Pdf2Img_convertor, Img2pdf_convertor
import werkzeug

app = Flask(__name__)
api = Api(app)

argument_parser = reqparse.RequestParser()
argument_parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files') 
# argument_parser.add_argument("input_path", type=str, location='form')

IP_PATH = "C:\Docusense-ML\src\data\PDF"
OP_PATH = "C:\Docusense-ML\src\data\output\pdf_to_png"


@app.route("/")
def hello_world():
    return jsonify({'hello': "Hello, World!"})


class Convert(Resource):
    def post(self):
        args = argument_parser.parse_args()
        Ip_pdf = args['file']
        # input_path = args['input_path']
        PdfConverter = Pdf2Img_convertor(IP_PATH,OP_PATH,pdf_file=Ip_pdf)
        output_png = PdfConverter.pdf_2_png()
        print('Completed')

        
        return "process completed"

api.add_resource(Convert,'/Convert/')

if __name__ == "__main__":
    app.run(debug=True,port=5001)