# Uni-Speak
This project demonstrates a web-based real-time object detection application using Flask, OpenCV, and YOLOv5. The system captures live video from a webcam, detects objects in real time using YOLOv5, and provides auditory feedback for detected objects using the SpeechSynthesis API.
# Features
Real-Time Object Detection: Captures live video from the webcam and detects objects in real time using YOLOv5.

Web Interface: Provides a user-friendly web interface to view the live video feed and detected objects.

Auditory Feedback: Uses the SpeechSynthesis API to read out the names of detected objects.

Interactive UI: Button to initiate object detection and display the results on the web page.
# Installation
## Prerequisites
Python 3.7+

Pip (Python package installer)

A webcam
## Clone the Repository
git clone https://github.com/ultralytics/yolov5.git

cd yolov5
## Install Dependencies
pip install -r requirements.txt
## Download YOLOv5 Model
This project uses the YOLOv5s model from the Ultralytics repository. It will be automatically downloaded when you run the code.
## Project Structure
server.py: Flask app script.

templates/index.html: HTML file for the web interface.

requirements.txt: Python dependencies.
## How It Works
Flask Server: Serves the web page and handles routes.

OpenCV: Captures video from the webcam.

YOLOv5: Detects objects in the video frames.

JavaScript: Manages user interactions and updates the UI.
# Example
Live Video Feed: Shows real-time webcam video.

Object Detection: Highlights and names of detected objects.

Auditory Feedback: Speaks the names of detected objects
