from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from source.Tesseract_Module import TextExraction
import werkzeug

app = Flask(__name__)
api = Api(app)

txt_parser = reqparse.RequestParser()
txt_parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files') 

IP_PATH = "C:\Docusense-ML\src\data\output\preprocess_images"
OP_PATH = "C:\Docusense-ML\src\data\output\preprocess_to_text"

@app.route("/")
def hello_world():
    return jsonify({'hello': "Hello, World!"})


class Tesseract(Resource):
    def post(self):
        pred = False
        args = txt_parser.parse_args()
        Ip_png = args['file']
        Imagetxt = TextExraction(IP_PATH,OP_PATH, png_file = Ip_png)
        output_txt = Imagetxt.png_to_text()
        
        return "Text Extraction completed"


api.add_resource(Tesseract,'/Tesseract/')

if __name__ == "__main__":
    app.run(debug=True,port=5003)