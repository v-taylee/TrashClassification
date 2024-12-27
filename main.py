from btn import Btn
from gpiozero import Button, LED, PWMLED
from model import TrashClassify
import cv2
from time import sleep
from PIL import Image
from datetime import datetime
from servo import ServoSet
import RPi.GPIO as GPIO
from enum import Enum

class Label(Enum):
    OTHER = 'other'
    PLASTIC = 'plastic'
    PAPER = 'paper'
    METAL = 'metal'

btn = Button(16)
model = TrashClassify("./model/model.tflite", "./model/labels.txt")

def take_pic():
    ip_cam_url = ""
    # Capture a frame from IP Camera
    cap = cv2.VideoCapture(ip_cam_url)
    
    if not cap.isOpened():
        print("can not connected camera")
    while (cap.isOpened()):
        ret, frame = cap.read()
        print("camera is open")
        if btn.is_pressed:
            cap.release()
            print("close")
            return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    print("close")
    cap.release()
    cv2.destroyAllWindows()

servo_set = ServoSet(4, 23)
led = PWMLED(26)
try:
    while True:
        led.value = 1
        img = take_pic()
        sleep(1)
        led.pulse() #running
        res = model.predict(img)
        index, label = res.split(" ")
        print(label)
        now = datetime.now()
        ts = now.timestamp()
        img.save(f"./output/{label}_{int(ts)}.jpg")
        if label == Label.OTHER.value:
            servo_set.backward()
        elif label == Label.PLASTIC.value:
            servo_set.right()
        elif label == Label.PAPER.value:
            servo_set.left()
        else:
            servo_set.forward()
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    GPIO.cleanup()
    
