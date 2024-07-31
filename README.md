# 🚦 Traffic Sign Recognition

## 🎯 Project Objective:
The project aims to develop a real-time traffic sign recognition system using a webcam. The main objective is to design and train a convolutional neural network (CNN) model capable of classifying different types of traffic signs. We have recently added voice recognition and text-to-speech conversion to our traffic sign recognition application. 🗣️➡️📢

## ⚙️ Technologies Used:
- **OpenCV**: The project involves using OpenCV for real-time capture and processing of traffic sign images. 🎥
- **Python**: Python is the primary programming language for the development of the entire project. 🐍
- **SpeechRecognition and pyttsx3**: The SpeechRecognition library is used for voice recognition, allowing the application to understand user voice commands. The pyttsx3 library is used for text-to-speech synthesis, announcing the classification result to the user. 🗣️📢

## 🚀 How the Project Works:
- **Model Training**: A CNN model is trained to recognize different types of traffic signs using a dataset containing over 35,000 images across 43 different classes. Training is done using TensorFlow and Keras. 🧠

- **Model Integration into the Application**: The pre-trained model is integrated into the application developed using OpenCV. The application captures real-time images from the webcam. 📸

- **Image Preprocessing**: Each captured image undergoes a preprocessing process, including grayscale conversion, histogram equalization, and normalization. ⚙️

- **Real-Time Classification**: The model classifies the preprocessed images in real-time, displaying the classification result on the webcam window. Information such as the detected class and probability is shown on the screen. 🖥️

- **Text-to-Speech**: To make the classification results accessible audibly, we integrated the pyttsx3 library for speech synthesis. 🔊

- **Voice Recognition**: Simultaneously, the system performs speech-to-text conversion using the SpeechRecognition library to understand user voice commands. Once the voice message is interpreted, the resulting text is clearly and legibly displayed on the screen. 🗣️➡️📜
