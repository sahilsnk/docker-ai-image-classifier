import os
import numpy as np
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array, load_img

app = Flask(__name__)

# Load the pre-trained MobileNetV2 model (this will download weights on the first run)
model = MobileNetV2(weights='imagenet')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', prediction="No image file part in the request.")
        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', prediction="No file selected.")
        if file:
            # Create the uploads directory if it doesn't exist
            upload_folder = os.path.join("static", "uploads")
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
            
            # Preprocess the image for MobileNetV2
            try:
                image = load_img(file_path, target_size=(224, 224))
            except Exception as e:
                return render_template('index.html', prediction=f"Error loading image: {e}")
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            image = preprocess_input(image)
            
            # Predict the image classification
            preds = model.predict(image)
            results = decode_predictions(preds, top=3)[0]
            prediction_text = ", ".join([f"{label}: {prob:.2f}" for (_, label, prob) in results])
            
            # Create a relative URL for the image
            image_url = "uploads/" + file.filename
            
            return render_template('index.html', prediction=prediction_text, image_url=image_url)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    # Run the app on all interfaces, port 5000, with debug mode enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
