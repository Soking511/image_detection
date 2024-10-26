
from paths import net, classfile_path
from flask import Flask, request, jsonify, send_file
from io import BytesIO
from detection import detect_objects
from flask_cors import CORS
import os
import cv2
from PIL import Image

app = Flask(__name__)
CORS(app)

# Route to handle the image upload and processing
@app.route('/upload', methods=['POST'])
def upload():
    if 'images' not in request.files:
        return jsonify({'error': 'No files provided'}), 400

    file = request.files['images']
    filepath = os.path.join('photos/uploads', file.filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    if img is None:
        return jsonify({'error': 'Unable to read the image file'}), 400
    result_img = detect_objects(img, net, classfile_path)

    cv2.imwrite(os.path.join('photos/uploads/processed', file.filename), result_img)
    _, img_encoded = cv2.imencode('.jpg', result_img)
    response_img = BytesIO(img_encoded.tobytes())

    return send_file(response_img, mimetype='image/jpeg')


if __name__ == '__main__':
    os.makedirs('photos/images', exist_ok=True)
    os.makedirs('photos/uploads', exist_ok=True)
    os.makedirs('photos/uploads/processed', exist_ok=True)
    app.run(port=8080)
