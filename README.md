# **AI-Powered Handwriting Recognition 📝🔍**  
**Convert handwritten text into digital text using AI, OCR, and Deep Learning!**  

---

## **📌 Project Overview**  
This AI-powered **Handwriting Recognition Tool** extracts handwritten text from images and converts it into **digital text** using **Computer Vision and Deep Learning**.  
It uses **Convolutional Neural Networks (CNNs)** for character recognition and **OCR (Optical Character Recognition)** for full text extraction.  

---

## **🚀 Features**  
✔ Extracts text from handwritten notes  
✔ Supports multiple handwriting styles  
✔ Web-based interface using Flask  
✔ Can process scanned documents and images  
✔ Expandable to support multiple languages  

---

## **🛠️ Technologies Used**  

| **Technology**  | **Purpose**  |  
|-----------------|-------------|  
| **Python**  | Main programming language |  
| **TensorFlow & Keras**  | AI model training |  
| **OpenCV**  | Image processing |  
| **Flask**  | Web app for uploading handwritten text |  
| **Pillow (PIL)**  | Image handling |  
| **Tesseract OCR**  | Optical character recognition |  

---

## **📂 Project Structure**  
```
/Handwriting_Recognition
│── model_training.py          # Train the handwriting recognition model
│── predict.py                  # Predict text from handwritten images
│── app.py                      # Flask Web Interface
│── static/sample_image.png     # Sample handwritten image
│── templates/index.html        # Web Interface
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```

---

## **🔧 Installation Guide**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/prangowda/AI-Powered-Handwriting-Recognition.git
cd AI-Powered-Handwriting-Recognition
```

### **2️⃣ Install Dependencies**  
```sh
pip install numpy tensorflow keras opencv-python flask pillow pytesseract
```

### **3️⃣ Install Tesseract OCR**  
Download and install **Tesseract OCR**:  
- **Windows**: [Download here](https://github.com/UB-Mannheim/tesseract/wiki)  
- **Linux (Ubuntu)**:  
  ```sh
  sudo apt install tesseract-ocr
  ```
- **Mac**:  
  ```sh
  brew install tesseract
  ```

### **4️⃣ Run Flask App**  
```sh
python app.py
```
Visit **http://127.0.0.1:5000/** to upload handwritten images.  

---

## **📜 How It Works**  

1. **User uploads a handwritten image**  
2. **CNN Model recognizes digits (0-9)** from handwritten text  
3. **OCR extracts full text** from the image  
4. **The output is displayed on the web app**  

---

## **📊 Sample Output**  

### **📷 Input Image**  
![Sample Image](static/sample_image.png)  

### **📝 Output**  
```
Predicted Digit: 3
Extracted Text: "Hello World!"
```

---

## **🔮 Future Enhancements**  
✅ Train the model to support **cursive handwriting**  
✅ Add **real-time handwriting recognition**  
✅ Deploy the model on a **mobile app**  
✅ Support **multiple languages**  

---

## **🤝 Contributing**  
We welcome contributions! Follow these steps:  
1. **Fork** the repository  
2. **Create** a new branch (`feature-xyz`)  
3. **Commit** your changes  
4. **Push** to your branch and submit a **Pull Request**  

