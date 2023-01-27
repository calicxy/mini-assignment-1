import os
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
from flask_cors import CORS
from check_file_similarity import get_checksum

app = Flask(__name__)
CORS(app)
uploads_dir = '/app/data'

@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        f1 = request.files['file1']
        f2 = request.files['file2']
        f1.save(os.path.join(uploads_dir, secure_filename(f1.filename)))
        f2.save(os.path.join(uploads_dir, secure_filename(f2.filename)))
        return 'file uploaded successfully\n'

@app.route('/checksum', methods=['GET'])
def determine_file_similarity():
    if request.method == 'GET':
        f1 = request.args.get('f1')
        f2 = request.args.get('f2')
        checksum_f1 = get_checksum(os.path.join(uploads_dir, str(f1)))
        checksum_f2 = get_checksum(os.path.join(uploads_dir, str(f2)))
        checksum_dict = {"f1_checksum":checksum_f1, "f2_checksum":checksum_f2, "equal_bool":checksum_f1==checksum_f2}
        return jsonify(checksum_dict)
        

if __name__ == '__main__':
    app.run(port=5001, 
            debug=True)
