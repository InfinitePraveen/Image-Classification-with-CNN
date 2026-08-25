# Image Classification with CNN

A complete TensorFlow/Keras computer-vision project that trains a Convolutional Neural Network (CNN) to classify CIFAR-10 images into 10 object categories.

## Project Highlights

- Kaggle CIFAR-10 dataset
- Exploratory data analysis and visualization
- Image normalization and train/validation split
- CNN architecture built with TensorFlow/Keras
- Data augmentation with random flipping, translation, rotation and zoom
- Model evaluation with accuracy, loss and confusion matrix
- Saved Keras model for inference
- Flask web application for image upload and prediction
- Responsive HTML/CSS/JavaScript frontend
- Six normal Jupyter notebooks covering the full workflow
- No `src/` package or custom data-loader/preprocessing/utils modules
- Contribution and changelog documentation

## Dataset

This project uses the Kaggle **CIFAR-10** dataset. CIFAR-10 contains 60,000 32×32 RGB images across 10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship and truck. The original split contains 50,000 training images and 10,000 test images.

Kaggle dataset:
https://www.kaggle.com/datasets/ayush1220/cifar10

Kaggle's official CIFAR-10 competition page:
https://www.kaggle.com/competitions/cifar-10

The dataset is not committed to this repository because the downloaded archive is large. Follow `data/README.md` for setup instructions.

## Repository Structure

```text
Image-Classification-with-CNN/
├── app.py
├── wsgi.py
├── requirements.txt
├── requirements-dev.txt
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda_and_visualization.ipynb
│   ├── 03_data_wrangling_and_augmentation.ipynb
│   ├── 04_cnn_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_inference_and_export.ipynb
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── models/
├── outputs/
├── templates/
├── static/
├── tests/
├── docs/
└── .github/
```

## Installation

```bash
git clone https://github.com/InfinitePraveen/Image-Classification-with-CNN.git
cd Image-Classification-with-CNN

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Notebook Workflow

Run notebooks in this order:

1. `01_data_exploration.ipynb` — inspect dataset shape, labels and samples.
2. `02_eda_and_visualization.ipynb` — class distribution and image analysis.
3. `03_data_wrangling_and_augmentation.ipynb` — normalization and augmentation.
4. `04_cnn_model_training.ipynb` — build and train the CNN.
5. `05_model_evaluation.ipynb` — evaluate accuracy, loss and confusion matrix.
6. `06_inference_and_export.ipynb` — export the model and verify predictions.

The notebooks intentionally contain the data loading, wrangling and preprocessing code directly. There is no custom `src/` module.

## Web App

After training and exporting the model:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Upload a 32×32 RGB image. The app resizes the image to the CNN input size and returns the predicted CIFAR-10 class with confidence.

If `models/cifar10_cnn.keras` does not exist, the app shows a setup message instead of failing silently.

## Model

Baseline architecture:

- Input: 32×32×3
- Rescaling
- Conv2D + BatchNormalization + ReLU
- Conv2D + BatchNormalization + ReLU
- MaxPooling + Dropout
- Conv2D + BatchNormalization + ReLU
- Conv2D + BatchNormalization + ReLU
- MaxPooling + Dropout
- Flatten
- Dense + Dropout
- 10-class Softmax output

Data augmentation is applied only during training.

## Expected Results

Exact results depend on hardware, TensorFlow version, random seed, training epochs and dataset handling. A properly trained baseline CNN should substantially outperform random guessing (10% accuracy) and provide a useful educational benchmark for CIFAR-10.

Do not hard-code a claimed accuracy in the repository unless it was produced by your own run.

## License

The source code in this repository is provided under the MIT License. Dataset terms remain governed by the relevant Kaggle/dataset terms; see `data/DATASET_LICENSE.md`.

## Author

**Praveen Kumar**

- GitHub: https://github.com/InfinitePraveen
- LinkedIn: https://www.linkedin.com/in/infinitepraveen/
