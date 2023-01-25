import requests
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

url = 'http://master:5555'

@app.route("/checksum-routetoapi", methods=['POST'])
def get_checksum():

    file1=request.files['file1']
    file2=request.files['file2']

    data = {
        'file1':(file1.filename, file1.stream, file1.content_type),
        'file2':(file2.filename, file2.stream, file2.content_type),
    }
    r = requests.post(url+'/upload', files=data)

    if r.status_code == 200:
        print('success!')
        params_arg = {'f1': file1.filename, 'f2':file2.filename}
        response = requests.get(url+'/checksum', params=params_arg)
        return response.json()

    else:
        return make_response("Could not upload files", 400)

if __name__ == '__main__':
    app.run(debug=True)