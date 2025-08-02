from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# ===== Model Load =====
model = load_model("Tumor.h5")

# ===== Class Names (fix order) =====
class_names = ['no', 'yes']

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    img_path = None

    if request.method == "POST":
        # ===== Image Upload =====
        img = request.files['file']
        img_path = os.path.join("static", img.filename)
        img.save(img_path)

        # ===== Prediction =====
        img = image.load_img(img_path, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction_array = model.predict(img_array)
        prediction = class_names[np.argmax(prediction_array)]

    return render_template("index.html", prediction=prediction, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
    app.py(debug=Trir )
