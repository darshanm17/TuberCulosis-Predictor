import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('model.h5')

def preprocess_image(image_path):
    IMG_SIZE = 224
    img = load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

def predict_tuberculosis(image_path):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    result = 'Tuberculosis' if prediction[0][0] > 0.5 else 'Normal'
    return result

# Example usage
image_path = r"C:\Users\DARSHAN M\OneDrive\Desktop\DataSet\train\TB\Tuberculosis\Tuberculosis-3.png"
prediction = predict_tuberculosis(image_path)
print(f'Prediction: {prediction}')
