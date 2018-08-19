import cv2
from flask import Flask, render_template, Response
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()        
    
    def get_frame(self):
        sampleNum = 0
        Id = 'xxa'
        while(True):
            success, img = self.video.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder
                cv2.imwrite("dataset/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
            #wait for 100 miliseconds 
            if sampleNum>20:
                break
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()
