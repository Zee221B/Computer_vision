<<<<<<< HEAD
# Computer Vision Rock Paper Scissors

# Table of Contents
1. [Introduction](#introduction)
2. [Section 1](#Setting up the environment)
3. [Section 2](#Creating the computer vision system)
4. [Section 3](#Installing the dependencies)
5. [Section 4](#Creating a Rock-Paper-Scissors game)
6. [Section 5](#Using the camera to play Rock-Paper-Scissors)
7. [Section 6](#Installation Instructions)
8. [Section 7](#Usage Instructions)
9. [Section 8](#License Information)
    
## Introduction

This project was built to improve my skills creating an interactive game, Rock-Paper-Scissors, one in which the user cna play with the computer using the camera.

## Setting up the environment

In this project, I use GitHub to track changes to my code and save them online in a GitHub repo. 

## Creating the computer vision system

I created an image project model with four different classes: Rock, Paper, Scissors or Nothing. I went to Teachable-Machine  to start creating the model. Each class was trained with images of myself showing each option to the camera. The "Nothing" class represented the lack of option in the image. The more images I trained with, the more accurate the model became.

### Installing the dependencies

To make the model work, I needed to make sure to complete the project on a Windows operating system, as some of the libraries used are not WSL friendly. I created a conda environment and then installed opencv-python, tensorflow, and ipykernel.
I activated the environment, and then installed pip by running the following command in my terminal conda install pip. Then, to install the rest of the libraries, i ran pip install <library>

I made sure to ipykernel by running the following command:

pip install ipykernel

Once I installed everything (regardless of the operating system) I created a requirements.txt file by running the following command:

pip list > requirements.txt

This file enables any other user that wants to use my computer to easily install these exact dependencies by running pip install requirements.txt.

I ran the following file to make sure the model I downloaded worked as expected:

import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
  *After the loop release the cap object
cap.release()
  *Destroy all the windows
cv2.destroyAllWindows()


## Creating a Rock-Paper-Scissors game

I created a Python script that will simulate a Rock-Paper-Scissors game, in which the code will ask me for an input then compare my input with the computer's choice to show the winner. 

I used the random module to pick a random option between rock, paper and scissors and input function to get the user's choice. I used if-elif-else statements so the script coudl choose a winner based on the classic rules of the game. I wrapped the codde in a function called get-winner and that returned the winner. This function took two arguments: computer_choice and user_choice.
If the computer wins, the function would print "You lost", if the user wins, the function would print "You won!", and if it's a tie, the function would print "It is a tie!".

## Using the camera to play Rock-Paper-Scissors

I replaced the hard-coded user guess with the output of the computer vision model. I created a new file called camera_rps.py where I wrote the new code.I created a new function called get_prediction that would return the output of the model I used earlier.The model can make many predictions at once if given many images. The game is repeated until either the user or the computer wins three rounds.

## Installation instructions

To carry out section 2 of this project, you will need to have VSCode installed on your machine, and within it opencv-python, tensorflow, and ipykernel and pip. 

## License information




