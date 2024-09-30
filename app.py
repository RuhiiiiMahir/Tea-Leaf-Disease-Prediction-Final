from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os 

app = Flask(__name__)

# Load the saved model
loaded_model = tf.keras.models.load_model('tea_sickness_model.h5')

# Define class labels
class_names = {0: 'Anthracnose', 1: 'algal leaf', 2: 'bird eye spot', 3: 'brown blight', 4: 'gray light', 5: 'healthy', 6: 'red leaf spot', 7: 'white spot'}

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400  # Return 400 Bad Request if no file is uploaded
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400  # Return 400 Bad Request if no file is selected
    if file:
        try:
            # Save the file to the server
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            
            # Load and preprocess the image
            img = image.load_img(file_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0  # Rescale pixel values to [0, 1]

            # Make predictions
            predictions = loaded_model.predict(img_array)
            predicted_class = np.argmax(predictions)

            # Get the predicted class name
            result = class_names[predicted_class]

            return jsonify({'prediction': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return 500 Internal Server Error on exception


# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
