# Face-Recognition-OpenCV

**Introduction**:

	This is a face recognition webapp and a python program. The webapp gets the video from 
	the webcam however you can input any video file manually. When the face is recognised 
	the frame of video gets saved into the local database.
	
# Installation :
		1. Install Python
		2. Install OpenCV
		3. Install Flask
		 Then Run Main.py through Cmd.
		 
# Methodology
		I used Opencv and HaarCascading for face detection.Here we will work with face 
		detection. In Haar-cascading the algorithm needs a lot of positive
		images (images of faces) and negative images (images without faces) to train 
		the classifier. Then we need to extract features from it. For
		this, Haar features shown in the below image are used. They are just like our 
		convolutional kernel.Each feature is a single value obtained by subtracting 
		sum of pixels under the white rectangle from sum of 
		pixels under the black rectangle.
	
**Resources**:
	
		- docs.opencv.org
		- http://flask.pocoo.org/docs/1.0/
		- www.pythonprogramming.net
		- https://github.com/log0/video_streaming_with_flask_example
		
**Step-Step Guide**

	> I created a simple html page for the video stream.
	
	> Then I used flask and python for the scripting of the page, how it will capture the live video 
	  from webcam.
	  
	> With flask I used render_teamplate to render the html page and for some other functions as well.
	
	> After creating the simple webcam stream, I used opneCV to produce the results.
	
	> I used haarcasacading and cascadeclassifier class for face detection and functios of opencv 
	to save the image fom video dtream with detected face.
