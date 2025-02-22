import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pytesseract

# Load trained model
model = load_model("handwriting_model.h5")

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))  # Resize to match model input
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=[0, -1])  # Reshape for CNN input
    return image

def predict_handwritten_text(image_path):
    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)
    predicted_digit = np.argmax(prediction)
    return predicted_digit

# OCR for full text recognition
def extract_text(image_path):
    return pytesseract.image_to_string(image_path)

if __name__ == "__main__":
    img_path = "static/sample_image.png"
    print("Predicted Digit:", predict_handwritten_text(img_path))
    print("Extracted Text:", extract_text(img_path))
