
# 🧠 Brain Tumor Prediction

This project uses deep learning techniques to predict and segment brain tumors from MRI images using Convolutional Neural Networks (CNN) and U-Net architectures.

---

## 📌 Features

- ✅ Brain tumor classification using CNN  
- ✅ Tumor segmentation using U-Net  
- ✅ Preprocessing and data augmentation  
- ✅ Performance evaluation with metrics  
- ✅ Easy-to-run scripts and modular code

---

## 📁 Project Structure

```
Brain_tumor_prediction-/
│
├── data/                # Dataset (MRI images)
├── notebooks/           # Jupyter notebooks for experiments
├── src/                 # Source scripts (models, utils, training)
│   ├── model/           # CNN and U-Net model architectures
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── inference.py
├── app.py               # Optional Flask/FastAPI app
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/ChiragJain-Codes/Brain_tumor_prediction-.git
cd Brain_tumor_prediction-
```

2. **Set up virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate    # On Linux/macOS
venv\Scriptsctivate       # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🧪 How to Use

### 🧹 Preprocess the data
```bash
python src/preprocess.py --input data/raw --output data/processed
```

### 🏋️‍♂️ Train the model
```bash
python src/train.py --model_type cnn --epochs 50
# or for segmentation
python src/train.py --model_type unet --epochs 100
```

### 📊 Evaluate
```bash
python src/evaluate.py --model weights/cnn_model.pth
```

### 🔍 Predict
```bash
python src/inference.py --model weights/cnn_model.pth --input sample_image.jpg
```

---

## 🧠 Model Architectures

| Model Type   | Description                     |
|--------------|----------------------------------|
| CNN          | For tumor classification         |
| U-Net        | For segmentation of tumor regions|

---

## 📈 Sample Results

> *(Add example image outputs and accuracy/dice scores here)*

---

## 🗃️ Dataset

This project uses public MRI datasets for brain tumor classification and segmentation. Common classes include:

- **Glioma Tumor**
- **Meningioma Tumor**
- **Pituitary Tumor**
- **No Tumor**

> *You can download a similar dataset from [Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) or your preferred source.*

---

## 🧾 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Chirag Jain**  
📬 [GitHub Profile](https://github.com/ChiragJain-Codes)

---

## ⭐️ Show your support

If you found this project useful, please give it a ⭐️ on GitHub!
