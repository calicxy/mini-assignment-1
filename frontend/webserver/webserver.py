import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
uploads_dir = '/home/vest1/Desktop/multi-01-starting-setup/backend/data'
url = 'https://127.0.0.1:5000'

@app.route("/checksum-routetoapi", methods=['POST'])
def get_checksum():
    param_dict = {
        'file1':request.form.get('file1'),
        'file2':request.form.get('file2')
    }
    # r = requests.post(url+'/checksum', data=param_dict)
    return jsonify({'file':{'name: ':'hey!', 'id':0, 'checksum':6784567834658}})
    return 'done?'
    # return response.json()

if __name__ == '__main__':
    app.run(debug=True)