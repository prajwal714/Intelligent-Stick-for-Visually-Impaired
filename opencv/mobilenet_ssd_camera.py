import numpy as np
import argparse
import os,time
try:
    import cv2 as cv
except ImportError:
    raise ImportError('Can\'t find OpenCV Python module. If you\'ve built it from sources without installation, '
                      'configure environemnt variable PYTHONPATH to "opencv_build_dir/lib" directory (with "python3" subdirectory if required)')

inWidth = 300
inHeight = 300
WHRatio = inWidth / float(inHeight)
inScaleFactor = 0.007843
meanVal = 127.5

classNames = ('background',
              'aeroplane', 'bicycle', 'bird', 'boat',
              'bottle', 'bus', 'car', 'cat', 'chair',
              'cow', 'diningtable', 'dog', 'horse',
              'motorbike', 'person', 'pottedplant',
              'sheep', 'sofa', 'train', 'tvmonitor')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="path to video file. If empty, camera's stream will be used")
    parser.add_argument("--prototxt", default="MobileNetSSD_deploy.prototxt",
                        help="path to caffe prototxt")
    parser.add_argument("-m", "--caffemodel", default="MobileNetSSD_deploy.caffemodel",
                        help="path to caffemodel file, download it here: "
                        "https://github.com/chuanqi305/MobileNet-SSD/")
    parser.add_argument("--thr", default=0.2, help="confidence threshold to filter out weak detections")
    args = parser.parse_args()

    net = cv.dnn.readNetFromCaffe(args.prototxt, args.caffemodel)

    cap = cv.VideoCapture(-1)
    counter=0
    while True:
        # Capture frame-by-frame
        counter+=1
        
        if(counter%10!=0):
            continue
            
        ret, frame = cap.read()
        frame = cv.flip( frame, 1 )
        
        blob = cv.dnn.blobFromImage(frame, inScaleFactor, (inWidth, inHeight), meanVal)
        net.setInput(blob)
        detections = net.forward()

        cols = frame.shape[1]
        rows = frame.shape[0]

        if cols / float(rows) > WHRatio:
            cropSize = (int(rows * WHRatio), rows)
        else:
            cropSize = (cols, int(cols / WHRatio))

        y1 = (rows - cropSize[1]) / 2
        y2 = y1 + cropSize[1]
        x1 = (cols - cropSize[0]) / 2
        x2 = x1 + cropSize[0]
        y1 = int(y1)
        y2 = int(y2)
        x1 = int(x1)
        x2 = int(x2)
        frame = frame[y1:y2,x1:x2]

        cols = frame.shape[1]
        rows = frame.shape[0]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > args.thr:
                class_id = int(detections[0, 0, i, 1])

                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop   = int(detections[0, 0, i, 5] * cols)
                yRightTop   = int(detections[0, 0, i, 6] * rows)
                x = (xLeftBottom+xRightTop)/2
                y = (yLeftBottom+yRightTop)/2
                xfinal=x
                yfinal=y
                if xfinal <= inWidth/3:
                    W_pos = "left "
                elif  xfinal <= (2*inWidth/3):
                    W_pos = "center "
                else:
                    W_pos = "right "
                        
                if yfinal <= (inHeight/3):
                    H_pos = "bottom "
                elif yfinal <= (2*inHeight/3):
                    H_pos = "mid "
                else:
                    H_pos = "top"

                cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                              (0, 255, 0))
                label = classNames[class_id]+H_pos+W_pos
                labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                cv.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                     (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                     (255, 255, 255), cv.FILLED)
                cv.putText(frame, label, (xLeftBottom, yLeftBottom),
                            cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
                print(label)
                #os.system("espeak ' "+label+" '")
                

       # break   

        cv.imshow("detections", frame)
        if cv.waitKey(1) >= 0:
           break
