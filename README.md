# 🚦 Reconnaissance de Panneaux de Signalisation

## 🎯 Objectif du Projet :
Le projet vise à développer un système de reconnaissance de panneaux de signalisation en temps réel à partir d'une webcam. L'objectif principal est de concevoir et d'entraîner un modèle de réseau neuronal convolutionnel (CNN) capable de classifier différents types de panneaux de signalisation. Nous avons récemment ajouté la reconnaissance vocale et la conversion texte-parole à notre application de reconnaissance de panneaux de signalisation. 🗣️➡️📢

## ⚙️ Technologies Utilisées :
- **OpenCV** : Le projet implique l'utilisation d'OpenCV pour la capture et le traitement en temps réel des images de panneaux de signalisation. 🎥
- **Python** : Python est le langage de programmation principal pour le développement de l'ensemble du projet. 🐍
- **SpeechRecognition et pyttsx3** : La bibliothèque SpeechRecognition est utilisée pour la reconnaissance vocale, permettant à l'application de comprendre les commandes vocales de l'utilisateur. La bibliothèque pyttsx3 est utilisée pour synthétiser la parole, annonçant le résultat de la classification à l'utilisateur. 🗣️📢

## 🚀 Fonctionnement du Projet :
- **Entraînement du Modèle** : Un modèle CNN est entraîné à reconnaître différents types de panneaux de signalisation à partir d'un ensemble de données contenant plus de 35 000 images de 43 classes différentes. L'entraînement est réalisé avec TensorFlow et Keras. 🧠

- **Intégration du Modèle dans l'Application** : Le modèle pré-entraîné est intégré dans l'application développée en utilisant OpenCV. L'application capture des images en temps réel à partir de la webcam. 📸

- **Prétraitement des Images** : Chaque image capturée est soumise à un processus de prétraitement, incluant la conversion en niveaux de gris, l'égalisation de l'histogramme, et la normalisation. ⚙️

- **Classification en Temps Réel** : Le modèle classifie en temps réel les images prétraitées, affichant le résultat de la classification sur la fenêtre de la webcam. Les informations, telles que la classe détectée et la probabilité, sont affichées à l'écran. 🖥️

- **Text_to_Speech** : Pour rendre les résultats de la classification accessibles de manière audible, nous avons intégré la bibliothèque pyttsx3 pour la synthèse vocale. 🔊

- **Reconnaissance Vocale** : Simultanément, le système effectue une conversion de la parole en texte en utilisant la bibliothèque SpeechRecognition pour comprendre les commandes vocales de l'utilisateur. Une fois le message vocal interprété, le texte résultant est affiché de manière claire et lisible à l'écran. 🗣️➡️📜
