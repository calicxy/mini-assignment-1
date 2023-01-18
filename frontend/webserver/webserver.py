import os
from werkzeug.utils import secure_filename
import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
uploads_dir = '/home/vest1/Desktop/multi-01-starting-setup/backend/data'

@app.route("/checksum-routetoapi")
param_dict = {
    'file1':request.form.get('file1'),
    'file2':request.form.get('file2')
}
requests.post(url, param_dict)

# post both files at once
# files saved into the data directory
@app.route('/upload', methods=['POST', 'GET'])
def upload_files():
    if request.method == 'GET':
        return 'Upload File Here:'
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        data = {'file1':f1,
                'file2':f2,
                }
        r = requests.post(url = API_ENDPOINT, data = data)
        return 'file uploaded successfully\n'

@app.route('/checksum', methods=['GET'])
def determine_file_similarity():
    if request.method == 'GET':
        f1 = request.args.get('f1')
        f2 = request.args.get('f2')
        payload = {'f1': f1, 'f2': f2}
        response = requests.get("http://127.0.0.1:5001", params=payload)
        return response.json()

if __name__ == '__main__':
    app.run(debug=True)