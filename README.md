# Intelligent-Stick-for-Visually-Impaired
## Introduction
This project was a part of out Btech Hardware Project. The main intent behind taking up this project is to help the blind 
people by providing them a navigation device through which they can visualize things in front of them and
can react accordingly with the help of the device. Our device gives an Audio feedback of the recognized Objects infront of it along 
with the approximate distance.

## Features of the Project
* Obstacle Detection, Classification and Localization.
* Voice Feedback through Earphones regarding the detected Obstacles.
* Distance Measuring using Ultrasonic Sensor.
* Live Video as well as Still Image capture using Pi Camera for processing.
* Push Buttons to choose specific mode while navigation.
## Technology Stack
* Python+Flask Server for API requests
* OpenCV for Image Recognition
* YOLO for Realtime Object Recognition
* MobileNet SSD 
* Heroku For Backend Deployment
## Hardware Components
* Rasperry Pi 3 Model B
* Ultrasonic Sensors HCSR04
* Raspberry Pi Camera V2
* Resistors, Push Buttons and Connecting Wires
* Battery Backup
## Architecture

## Working
In this project we will be processing images taken through Pi Camera mounted on our
smart Navigation Stick. In the Object Detection Mode the Obstacles in front of the
blind person will be captured, the results of image processing will consist of Detected
Objects along with their spatial location. We will be processing still images using our
self developed API hosted on Heroku, the results will then be converted to an
audio feedback using python ESpeak module and will be fed into the earphones of the
user. The live video will be processed using OpenCV libraries and SSD MobileNet
Lite algorithm on real time frames to produce detections.This mode is active when we
press the Navigation button on the stick.


