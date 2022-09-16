from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from source.Preprocessing import Image_Preprocess
import werkzeug

app = Flask(__name__)
api = Api(app)

png_parser = reqparse.RequestParser()
png_parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files') 
# png_parser.add_argument("input_path", type=str, location='form')

IP_PATH = "C:\Docusense-ML\src\data\output\pdf_to_png"
OP_PATH = "C:\Docusense-ML\src\data\output\preprocess_images"

@app.route("/")
def hello_world():
    return jsonify({'hello': "Hello, World!"})


class Preprocess(Resource):
    def post(self):
        args = png_parser.parse_args()
        Ip_png = args['file']
        # input_path = args['input_path']
        ImagePreprocess = Image_Preprocess(Ip_png,OP_PATH)
        output_png = ImagePreprocess.png_preprocess()
        return "process completed"


api.add_resource(Preprocess,'/Preprocess/')

if __name__ == "__main__":
    app.run(debug=True,port=5003)