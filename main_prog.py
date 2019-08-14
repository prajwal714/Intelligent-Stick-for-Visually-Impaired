import object_detection_mode
import mobilenet
import distance
import RPi.GPIO as GPIO
import os,time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)




distance.init()
pressed = 0

try:
    while True:
        while GPIO.input(22) == 1:
            print("main button on")
            GPIO.output(33,GPIO.LOW)
            time.sleep(1)
            GPIO.output(40,GPIO.HIGH)
            print("main LED on")
            mobilenet.mobilenet()
        while GPIO.input(22) == 0:
            
            
            print (" main LED off")
            print("secondary LED on")
            GPIO.output(40,GPIO.LOW)
            time.sleep(1)
            GPIO.output(33,GPIO.HIGH)
            if GPIO.input(10) == 1 and pressed == 0:
                pressed = 1
                
                
                print("secondary button pushed")
                object_detection_mode.captureImage()
                os.system("espeak ' " + "Obstacle at Distance "+ str(int(distance.distance())) +" centimeters'")
                print(int(distance.distance()))
            elif GPIO.input(10) == 0:
                pressed = 0

except KeyboardInterrupt:
    GPIO.output(40,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.cleanup()