Crop Disease Analysis using Deep Learning 🌿🧪

OVERVIEW
This project aims to identify and classify crop diseases using Convolutional Neural Networks (CNNs). The model processes images of crop leaves to detect nutrient deficiencies such as:

1) Nitrogen Deficiency
2) Phosphorus Deficiency
3) Potassium Deficiency
4) Healthy Leaves
   
DATASET
The dataset is stored in Google Drive under the folder '/content/drive/MyDrive/HARN RICE DS'. It consists of images categorized into different nutrient deficiency classes.

TECHNOLOGIES USED
➢ Python
➢ TensorFlow & Keras (Deep Learning Framework)
➢ Matplotlib (Visualization)
➢ Scikit-learn (Data Preprocessing)

PROJECT OVERFLOW

Dataset Loading & Augmentation
● Images are loaded from Google Drive.
● Augmentation techniques such as rotation, width/height shift, shear, and zoom are applied to increase model robustness.

CNN Model Architecture
● 3 Convolutional Layers with ReLU activation & MaxPooling.
● Fully Connected Layers with Dropout for regularization.
● Softmax activation for multi-class classification.

Model Training & Evaluation
● The model is trained for 20 epochs.
● Accuracy & Loss are visualized for training and validation sets.

Prediction Functionality
● Users can upload an image of a leaf.
● The model predicts the deficiency class with confidence scores.
● The image is displayed along with the predicted class.

Results
The trained model achieves high accuracy in classifying crop diseases. Predictions are displayed with confidence scores.

Future Enhancements
-> Support for more crop types.
-> Deploy as a web or mobile app for farmers.
-> Improve accuracy with transfer learning models like EfficientNet.
