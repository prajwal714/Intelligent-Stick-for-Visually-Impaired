# Intelligent-Stick-for-Visually-Impaired
**Product Image**


<img src="/images/navigation-stick.png" height="500">

## Introduction
This project was a part of out Btech Hardware Project in our Sophmore Year. The main intent behind taking up this project is to help the blind 
people by providing them a navigation device through which they can visualize things in front of them and
can react accordingly with the help of the device. Our device gives an Audio feedback of the recognized Objects infront of it along 
with the approximate distance.
I along with my batchmate Aman Rai were involved in building this project from scratch. This bagged one of the best projects title in our showcase and presentation. 


## Features: 
* Obstacle Detection, Classification and Localization.
* Voice Feedback through Earphones regarding the detected Obstacles.
* Distance Measuring using Ultrasonic Sensor.
* Live Video as well as Still Image capture using Pi Camera for processing.
* Push Buttons to choose specific mode while navigation.

**Detailed Thesis and working has been provided in the thesis report in the Repository.**
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

<img src="/images/final_deployed_view.jpg" width="500">


## Results


<p align="center">
    <img src="/images/testImages.png" alt="test Images" width="700">
<img src="/images/testResults.png" alt="test Results" width="700">
  </p>




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

## About me
I am Computer Science Undergrad from IIIT Gwalior. Former intern at GoJek, passionate dev and tech enthusiast. I keep myself involved in building stuff and experimenting with new things. Do checkout my portfolio and connect with me on LinkedIn. 
- **Portfolio** : <a href="https://prj-prajwal.netlify.app/" target="_blank">`prj-prajwal.netlify.app`</a>
- **LinkedIn** <a href="https://www.linkedin.com/in/prajwal714/" target="_blank">`linkedin.com/in/prajwal714`</a>



