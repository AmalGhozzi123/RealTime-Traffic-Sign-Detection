import cv2
import numpy as np
import os
import tensorflow as tf
import speech_recognition as sr
import threading
import pyttsx3
import time

frameWidth = 640
frameHeight = 480
brightness = 180
threshold = 0.90
font = cv2.FONT_HERSHEY_SIMPLEX
recognizer = sr.Recognizer()

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)

model = tf.keras.models.load_model(r'C:\Users\amalg\PycharmProjects\Mini_Project\TrafficSigns\model.h5')

# Variable de drapeau pour indiquer si la détection d'image est en cours
image_detection_in_progress = True

# Temps d'attente pour la détection des panneaux (en secondes)
detection_time = 900  # 5 minutes

# Temps initial
start_detection_time = time.time()

# Initialiser l'interface graphique pour la reconnaissance vocale
interface_img = np.zeros((500, 500, 3), dtype=np.uint8)

def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

def getClassName(classNo):
    if classNo == 0:
        return 'Speed Limit 20 km/h'
    elif classNo == 1:
        return 'Speed Limit 30 km/h'
    elif classNo == 2:
        return 'Speed Limit 50 km/h'
    elif classNo == 3:
        return 'Speed Limit 60 km/h'
    elif classNo == 4:
        return 'Speed Limit 70 km/h'
    elif classNo == 5:
        return 'Speed Limit 80 km/h'
    elif classNo == 6:
        return 'End of Speed Limit 80 km/h'
    elif classNo == 7:
        return 'Speed Limit 100 km/h'
    elif classNo == 8:
        return 'Speed Limit 120 km/h'
    elif classNo == 9:
        return 'No passing'
    elif classNo == 10:
        return 'No passing for vechiles over 3.5 metric tons'
    elif classNo == 11:
        return 'Right-of-way at the next intersection'
    elif classNo == 12:
        return 'Priority road'
    elif classNo == 13:
        return 'Yield'
    elif classNo == 14:
        return 'Stop'
    elif classNo == 15:
        return 'No vechiles'
    elif classNo == 16:
        return 'Vechiles over 3.5 metric tons prohibited'
    elif classNo == 17:
        return 'No entry'
    elif classNo == 18:
        return 'General caution'
    elif classNo == 19:
        return 'Dangerous curve to the left'
    elif classNo == 20:
        return 'Dangerous curve to the right'
    elif classNo == 21:
        return 'Double curve'
    elif classNo == 22:
        return 'Bumpy road'
    elif classNo == 23:
        return 'Slippery road'
    elif classNo == 24:
        return 'Road narrows on the right'
    elif classNo == 25:
        return 'Road work'
    elif classNo == 26:
        return 'Traffic signals'
    elif classNo == 27:
        return 'Pedestrians'
    elif classNo == 28:
        return 'Children crossing'
    elif classNo == 29:
        return 'Bicycles crossing'
    elif classNo == 30:
        return 'Beware of ice/snow'
    elif classNo == 31:
        return 'Wild animals crossing'
    elif classNo == 32:
        return 'End of all speed and passing limits'
    elif classNo == 33:
        return 'Turn right ahead'
    elif classNo == 34:
        return 'Turn left ahead'
    elif classNo == 35:
        return 'Ahead only'
    elif classNo == 36:
        return 'Go straight or right'
    elif classNo == 37:
        return 'Go straight or left'
    elif classNo == 38:
        return 'Keep right'
    elif classNo == 39:
        return 'Keep left'
    elif classNo == 40:
        return 'Roundabout mandatory'
    elif classNo == 41:
        return 'End of no passing'
    elif classNo == 42:
        return 'End of no passing by vechiles over 3.5 metric tons'

def voice_recognition_interface():
    while True:
        cv2.imshow("Voice Recognition", interface_img)
        cv2.waitKey(1)

def voice_recognition():
    while image_detection_in_progress:
        try:
            with sr.Microphone() as source:
                print("Say something:")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=15)
                recognized_text = recognizer.recognize_google(audio)
                print("You said: " + recognized_text)
                update_text(recognized_text)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results Speech Recognition service; {0}".format(e))
def update_text(text):
    global interface_img
    interface_img = np.zeros((500, 500, 3), dtype=np.uint8)
    cv2.putText(interface_img, f"Last Recognized: {text}", (10, 30), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)

def speak_out(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def close_camera():
    # Fermer la caméra
    cap.release()
    cv2.destroyAllWindows()

# Lancer le thread pour la reconnaissance vocale
voice_thread = threading.Thread(target=voice_recognition)
voice_thread.start()

# Lancer le thread pour l'interface graphique de la reconnaissance vocale
interface_thread = threading.Thread(target=voice_recognition_interface)
interface_thread.start()

# ... (le reste du code reste inchangé)

while image_detection_in_progress:
    # Calculer le temps écoulé pour la détection des panneaux
    elapsed_detection_time = time.time() - start_detection_time

    if elapsed_detection_time > detection_time:
        # Arrêter la détection des panneaux après 5 minutes
        image_detection_in_progress = False

    success, imgOrignal = cap.read()
    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 32, 32, 1)
    cv2.putText(imgOrignal, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)

    predictions = model.predict(img)
    classIndex = np.argmax(predictions, axis=1)
    probabilityValue = np.amax(predictions)

    class_name = getClassName(classIndex)
    cv2.putText(imgOrignal, str(classIndex) + " " + str(class_name), (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, str(round(probabilityValue * 100, 2)) + "%", (180, 75), font, 0.75, (0, 0, 255), 2,
                cv2.LINE_AA)

    if probabilityValue > threshold:
        speak_out(f"The detected class is {class_name}")

    cv2.imshow("Result", imgOrignal)

    # Attendre 1 milliseconde pour vérifier si l'utilisateur a appuyé sur une touche
    key = cv2.waitKey(1) & 0xFF

    # Si l'utilisateur appuie sur 'q', sortir de la boucle
    if key == ord('q'):
        break

# Libérer la caméra dans le bloc finally
try:
    # Attendre la fin du thread de reconnaissance vocale
    voice_thread.join()
finally:
    # Fermer la caméra et afficher l'interface
    close_camera()

    # Attendre la fin du thread de l'interface graphique
    interface_thread.join()

    # Libérer les ressources
    cv2.destroyAllWindows()