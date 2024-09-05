import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
from gtts import gTTS
import pygame
import os

# Read image
image_path = r"image/path"  # Use raw string for Windows file path
img = cv2.imread(image_path)

# Instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# Detect text on image
text_ = reader.readtext(img)

threshold = 0.25
detected_text = []

# Draw bounding boxes and collect text
for t_, t in enumerate(text_):
    bbox, text, score = t
    if score > threshold:
        # Convert bbox to integer coordinates if needed
        bbox = np.array(bbox).astype(int)

        # Draw bounding box
        cv2.rectangle(img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)

        # Put text
        cv2.putText(img, text, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

        # Collect text for TTS
        detected_text.append(text)

# Display the image with bounding boxes
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axes for better visualization
plt.show()

# Combine all detected texts into a single string
full_text = ' '.join(detected_text)

# Convert text to speech
tts = gTTS(text=full_text, lang='en', slow=False)
audio_path = 'output.mp3'
tts.save(audio_path)

# Play the audio file
pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

# Wait until the audio is finished playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Clean up
os.remove(audio_path)
