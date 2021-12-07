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
import time 
import os
import json
# dotenv
from dotenv import load_dotenv
load_dotenv()

# dotenv initial values
CAMERA_STREAM_URLS = os.getenv("RASP_CAMERA_URLS", "http://127.0.0.1:5000/stream").split(",")