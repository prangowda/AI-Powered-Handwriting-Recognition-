from flask import Flask, render_template, request
from predict import predict_handwritten_text, extract_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file:
            image_path = "static/uploaded_image.png"
            uploaded_file.save(image_path)

            # Predict text
            predicted_digit = predict_handwritten_text(image_path)
            extracted_text = extract_text(image_path)

            return render_template("index.html", digit=predicted_digit, text=extracted_text)

    return render_template("index.html", digit=None, text=None)

if __name__ == "__main__":
    app.run(debug=True)
