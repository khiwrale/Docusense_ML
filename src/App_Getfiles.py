from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from source.Files import files
import werkzeug

app = Flask(__name__)
api = Api(app)

argument_parser = reqparse.RequestParser()
# argument_parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files') 
argument_parser.add_argument("input_path", type=str, location='form')


@app.route("/")
def hello_world():
    return jsonify({'hello': "Hello, World!"})


class Get_Files(Resource):
    def post(self):
        args = argument_parser.parse_args()
        # Ip_pdf = args['file']
        input_path = args['input_path']
        Files_in_folder = files(input_path)
        # if Files_in_folder == []:
        #     print('Folder is empty')
        # else:
        #     print(Files_in_folder)
        return files(input_path)


api.add_resource(Get_Files,'/Files/')

if __name__ == "__main__":
    app.run(debug=True,port=5097)