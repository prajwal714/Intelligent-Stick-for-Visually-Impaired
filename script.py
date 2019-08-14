# import the necessary packages
import requests
import os,time
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# initialize the Keras REST API endpoint URL along with the input
# image path
camera = PiCamera()
camera.vflip=True
rawCapture = PiRGBArray(camera)

KERAS_REST_API_URL = "https://objectdetection407.herokuapp.com/predict"
IMAGE_PATH = "image.jpg"

time.sleep(5)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
print(image)
# display the image on screen and wait for a keypress
camera.stop_preview()
camera.close()
cv2.imwrite("image.jpg", image)
cv2.waitKey(0)
# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()

payload = {"image": image}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

# ensure the request was successful
if r["success"]:
    # loop over the predictions and display them
    for (i, result) in enumerate(r["predictions"]):
        print(result["label"],result["x"],result["y"])
        os.system("espeak ' " + result["label"]+result["y"]+result["x"]+" '")
# otherwise, the request failed
else:
    print("Request failed")
