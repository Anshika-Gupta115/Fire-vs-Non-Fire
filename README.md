# 🔥 Fire vs Non-Fire Detection Using Deep Learning

## 📌 Project Overview

This project is a Deep Learning-based Fire vs Non-Fire Image Classification System built using Python and TensorFlow/Keras. It classifies images into two categories: Fire and Non-Fire using Convolutional Neural Networks (CNN).

The project implements two different approaches: a custom CNN model built from scratch and MobileNetV2 using Transfer Learning with pre-trained ImageNet weights.

Both models are trained and evaluated to compare their performance. MobileNetV2 achieved better classification results with **97% accuracy**.

## 🎯 Objectives

- Develop a Deep Learning model to classify images as Fire or Non-Fire.
- Build a custom CNN architecture from scratch for binary image classification.
- Apply Transfer Learning using the pre-trained MobileNetV2 architecture.
- Perform image preprocessing and normalization.
- Compare CNN and MobileNetV2 based on accuracy, precision, recall, and F1-score.
- Develop an interactive application for fire image classification.

## 🛠️ Technologies Used

- Python – Programming language
- TensorFlow & Keras – Deep Learning model development and training
- CNN – Image classification architecture
- MobileNetV2 – Pre-trained CNN architecture for Transfer Learning
- NumPy – Numerical operations and array manipulation
- Pandas – Dataset handling and analysis
- Matplotlib – Data visualization
- Seaborn – Confusion matrix visualization
- Scikit-learn – Dataset splitting and model evaluation
- Pillow (PIL) – Image loading and processing
- Streamlit – Web application interface

## 🔥 Input Classes

The model classifies images into two categories:

- Fire (1): Images containing fire.
- Non-Fire (0): Images without fire.

## ⚙️ How It Works

1. Load and explore the Fire and Non-Fire image dataset.
2. Analyze the image distribution and dataset structure.
3. Split the dataset into 80% training and 20% testing data using stratified sampling.
4. Resize images to 224 × 224 pixels.
5. Convert images into RGB format and normalize pixel values between 0 and 1.
6. Train a custom CNN model from scratch.
7. Implement MobileNetV2 using pre-trained ImageNet weights.
8. Evaluate both models using accuracy, precision, recall, F1-score, and confusion matrices.
9. Save the trained MobileNetV2 model for further use.

## 🧠 Model Architectures

### 1. CNN from Scratch

A custom Convolutional Neural Network is developed using Keras Sequential API.

The architecture includes:

- Three convolutional layers with 32, 64, and 128 filters.
- MaxPooling2D layers for dimensionality reduction.
- Global Average Pooling.
- Dropout layer (0.3) to help reduce overfitting.
- Sigmoid output layer for binary classification.

## Training Configuration:
 
| Parameter      | Value               |
| Input Size     | 224 × 224 × 3       |
| Optimizer      | Adam                |
| Learning Rate  | 0.001               |
| Loss Function  | Binary Crossentropy |
| Maximum Epochs | 15                  |
| Batch Size     | 32                  |
| Early Stopping | Used                |

### 2. MobileNetV2 – Transfer Learning

MobileNetV2 is used with pre-trained ImageNet weights to extract image features.

The original classification head is removed, and custom classification layers are added.

## Architecture Components:

- Pre-trained MobileNetV2 base model.
- ImageNet weights.
- Frozen base model during training.
- Global Average Pooling layer.
- Dropout layer (0.3).
- Dense output layer with sigmoid activation.

Training Configuration:

| Parameter | Value |
| Input Size | 224 × 224 × 3 |
| Pre-trained Weights | ImageNet |
| Base Model | Frozen |
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Loss Function | Binary Crossentropy |
| Epochs | 10 |
| Batch Size | 32 |

## 📊 Model Performance

Both models are evaluated using classification reports and confusion matrices.

### CNN from Scratch

| Metric    | Non-Fire | Fire |
| Precision | 89%      | 95% |
| Recall    | 96%      | 86% |
| F1-Score  | 93%      | 90% |

Overall Accuracy: 92%

### MobileNetV2 – Transfer Learning

| Metric | Non-Fire | Fire |
|---|---:|---:|
| Precision | 96% | 98% |
| Recall | 98% | 96% |
| F1-Score | 97% | 97% |

**Overall Accuracy: 97%**

### Model Comparison

| Evaluation Metric | CNN | MobileNetV2 
| Accuracy          | 92% | 97% |
| Fire Precision    | 95% | 98% |
| Fire Recall       | 86% | 96% |
| Fire F1-Score     | 90% | 97% |

MobileNetV2 performed better than the custom CNN across the reported evaluation metrics.

## 🌟 Key Features

- Binary classification of Fire and Non-Fire images.
- Two model architectures implemented and compared.
- Transfer Learning using ImageNet pre-trained MobileNetV2.
- Automated image preprocessing and normalization.
- Model evaluation using classification reports.
- Confusion matrix visualization.
- Saved trained model for application use.
- Interactive Streamlit-based image classification interface.

## 📂 Project Structure


Fire-Non-Fire-Detection/
│
├── data/
│   ├── Train_Data/
│   │   ├── Fire/
│   │   └── Non_Fire/
│   │
│   └── Test_Data/
│       ├── Fire/
│       └── Non_Fire/
│
├── app.py
├── mobilenet_fire_model.h5
├── fire_vs_non_fire_model.ipynb
├── requirements.txt
├── README.md
└── .gitignore


## 🚀 Installation and Setup

### 1. Clone the Repository


git clone <https://github.com/Anshika-Gupta115/Fire-vs-Non-Fire>
cd Fire-Non-Fire-Detection


### 2. Install Dependencies


pip install -r requirements.txt

### 3. Run the Application


python -m streamlit run app.py


The Streamlit application will open in your web browser.

## 🔮 Future Improvements

- Improve fire detection performance using a larger and more diverse dataset.
- Fine-tune MobileNetV2 to further improve classification performance.
- Implement real-time fire detection using video streams.
- Add automated fire alerts and notification features.
- Explore Grad-CAM for visual explanation of model predictions.
- Optimize the model for edge devices such as Raspberry Pi.

## ⚠️ Limitations

- The model is trained for binary Fire and Non-Fire image classification.
- Predictions depend on the quality and diversity of the training dataset.
- The current model classifies images and does not independently track fire movement or estimate fire size.
- Performance on real-world images may differ from the reported evaluation results.

## 👩‍💻 About the Author

Anshika Gupta
BCA Final Year Student | Aspiring AI/ML Engineer

Passionate about Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision, with hands-on experience in developing intelligent, data-driven applications. Focused on building practical AI solutions, exploring advanced deep learning techniques, and continuously strengthening skills in Python, predictive modeling, and real-world problem-solving.

Areas of Interest: Artificial Intelligence | Machine Learning | Deep Learning | Computer Vision | Data Science