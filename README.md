# 🚦 Traffic Sign Recognition

## 🎯 Project Objective 
The project aims to develop a real-time traffic sign recognition system using a webcam. The main objective is to design and train a convolutional neural network (CNN) model capable of classifying different types of traffic signs. We have recently added voice recognition and text-to-speech conversion to our traffic sign recognition application. 🗣️➡️📢


## ⚙️ Technologies Used

- **Python** : Python is the primary programming language for the development of the entire project. 🐍

### Libraries
- **OpenCV** : The project involves using OpenCV for real-time capture and processing of traffic sign images. 🎥
- **SpeechRecognition** : The SpeechRecognition library is used for voice recognition, allowing the application to understand user voice commands. 🗣️
- **pyttsx3** : The pyttsx3 library is used for text-to-speech synthesis, announcing the classification result to the user. 📢
- **TensorFlow** : TensorFlow is used to train the CNN model for traffic sign classification. 🧠
- **Keras**  : Keras is used as the high-level API for building and training the CNN model. ⚙️
- **NumPy**  : NumPy is used for numerical operations and array manipulation during image processing and model training. 🔢
- **os**  : The os library is used for file and directory operations, such as loading and saving model files. 📁
- **threading**  : The threading library is used for handling concurrent operations, like running voice recognition and image processing simultaneously. ⏳
- **time**  : The time library is used for managing timing operations, like setting intervals for processing and waiting. ⏲️


## 🚀 How the Project Works 
- **Model Training** : A CNN model is trained to recognize different types of traffic signs using a dataset containing over 35,000 images across 43 different classes. Training is done using TensorFlow and Keras. 🧠

- **Model Integration into the Application**: The pre-trained model is integrated into the application developed using OpenCV. The application captures real-time images from the webcam. 📸

- **Image Preprocessing** : Each captured image undergoes a preprocessing process, including grayscale conversion, histogram equalization, and normalization. ⚙️

- **Real-Time Classification** : The model classifies the preprocessed images in real-time, displaying the classification result on the webcam window. Information such as the detected class and probability is shown on the screen. 🖥️

- **Text-to-Speech** : To make the classification results accessible audibly, we integrated the pyttsx3 library for speech synthesis. 🔊

- **Voice Recognition**: Simultaneously, the system performs speech-to-text conversion using the SpeechRecognition library to understand user voice commands. Once the voice message is interpreted, the resulting text is clearly and legibly displayed on the screen. 🗣️➡️📜

## 🚀 How to Deploy the Project
1. **Clone the Repository**
   `git clone https://github.com/AmalGhozzi123/RealTime-Traffic-Sign-Detection.git`
2. **Install Dependencies**
- Make sure you have Python 3.6 or higher installed on your system.
also Make sure you have the following libraries installed. You can install them using pip:
- **For OpenCV :**
  `pip install opencv-python`
- **For TensorFlow :**
  `pip install tensorflow`
- **For For Keras :**
  `pip install keras`
- **For SpeechRecognition :**
  `pip install SpeechRecognition`
- **For pyttsx3 :**
  `pip install pyttsx3`
- **For numpy :**
  `pip install numpy`
  
## 🧩 Additional Information
Feel free to modify and extend this project to suit your needs. If you encounter any issues or need further assistance, you can contact me at amalghozzi@outlook.com.
