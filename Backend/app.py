from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Define the upload folder - adjust the path as needed
upload_folder = os.path.join(os.getcwd(), 'uploads')

# Create the uploads directory if it doesn't exist
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

# Load the trained model
model_path = './model.h5'  # Adjust the path as necessary
model = tf.keras.models.load_model(model_path)

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

# Function to preprocess image
def preprocess_image(image_path):
    IMG_SIZE = 224
    img = load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Function to predict tuberculosis
def predict_tuberculosis(image_path):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    result = 'Tuberculosis' if prediction[0][0] > 0.5 else 'Normal'
    return result

@app.route('/upload', methods=['POST'])
@cross_origin()  # Allow CORS for this endpoint
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        prediction = predict_tuberculosis(file_path)
        
        return jsonify({
            'filename': filename,
            'prediction': prediction
        }), 200
    else:
        return jsonify({'error': 'File type not allowed. Allowed extensions: png, jpg, jpeg'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
