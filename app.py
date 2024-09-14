import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import rasterio
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'tif','png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        elevation_data, width, height = process_dtm(filepath)
        return {
            "elevation_data": elevation_data.tolist(),
            "width": width,
            "height": height
        }

    return redirect(url_for('index'))

def process_dtm(filepath):
    with rasterio.open(filepath) as dataset:
        elevation_data = dataset.read(1)
    
    min_val, max_val = elevation_data.min(), elevation_data.max()
    normalized_data = (elevation_data - min_val) / (max_val - min_val)
    
    return normalized_data.flatten(), elevation_data.shape[1], elevation_data.shape[0]

if __name__ == '__main__':
    app.run(debug=True)
