# THIS CODE IS TAKEN FROM https://www.analyticsvidhya.com/blog/2020/04/vehicle-detection-opencv-python/
# YTU CDTP Vehicle Stays Highway Anomaly Detection
# Author: Alper Reha YAZGAN
# Date: 08.12.2021

#
#   Anomaly Detection Documentation: https://www.analyticsvidhya.com/blog/2020/04/vehicle-detection-opencv-python/
#   It checks if vehicle exit from highway line and record video
#   - Vehicle abandon from highway detection
#   - Vehicle speed detection

#
#   APP INTERNAL DEPENDENCIES
#
import os
# dotenv
from dotenv import load_dotenv
load_dotenv()

#
#   OPENCV DEPENDENCIES
#

import cv2
# print opencv version
print("OpenCV version: {}".format(cv2.__version__))

# path to video and cascade model
cascade_src = os.path.join(os.getcwd(), 'haarcascades','cars.xml')
video_src = os.path.join(os.getcwd(), 'samples','highway-nonanomaly.mp4')

# print paths
print("Cascade path: {}".format(cascade_src))
print("Video path: {}".format(video_src))

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

    

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # highway line borders
    # left border is 1/4 of the screen width, right border is 3/4 of the screen width. 
    # Notify with blue line
    cv2.line(img, (int(img.shape[1]/5), 0), (int(img.shape[1]/5), img.shape[0]), (255, 0, 0), 2)
    cv2.line(img, (int(img.shape[1]*4/5), 0), (int(img.shape[1]*4/5), img.shape[0]), (255, 0, 0), 2)


    for (x,y,w,h) in cars:
        # check if vehicle exit from highway line (left border or right border)
        # if attached to left border, vehicle is leaving from highway red box
        # if attached to right border, vehicle is leaving from highway red box
        # otherwise, vehicle is staying on highway green box
        if (x < int(img.shape[1]/5)):
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            pass
        elif (x > int(img.shape[1]*4/5)):
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            pass
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            pass   
    cv2.imshow('YTU-CDTP-HIGHWAY', img)

    # check cars object (x,y,w,h) if exit highway line
    # if exit highway line, record video
    """
    if (len(cars) > 0):
        # check cars position if exit highway line
        for (x,y,w,h) in cars:
            if (y < 100):
                # record video
                print("Anomaly detected!")
                # create video name
                video_name = "video_" + str(time.time()) + ".mp4"
                # create video path
                video_path = os.path.join(os.getcwd(), 'videos', video_name)
                # create video writer
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(video_path, fourcc, 20.0, (640,480))
                # record video
                while True:
                    ret, img = cap.read()
                    if (type(img) == type(None)):
                        break
                    out.write(img)
                # close video writer
                out.release()
                # exit loop
                break
            pass
        pass
    """
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()