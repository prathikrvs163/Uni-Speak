import torch
import cv2
from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)
cap = cv2.VideoCapture(0)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Set desired confidence threshold
CONFIDENCE_THRESHOLD = 0.4


def detect_objects(frame):
    results = model(frame)
    detected_objects = []

    for obj in results.xyxy[0].tolist():
        x1, y1, x2, y2, score, class_id = obj[:6]
        if score > CONFIDENCE_THRESHOLD:
            class_name = model.names[int(class_id)]
            detected_objects.append(class_name)
            label = f'{class_name} {score:.2f}'
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame, detected_objects


def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame, _ = detect_objects(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/detect', methods=['POST'])
def detect():
    success, frame = cap.read()
    if success:
        frame, detected_objects = detect_objects(frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        response = {
            'detected_objects': detected_objects,
            'image': buffer.tobytes().decode('latin1')
        }
        return jsonify(response)
    return jsonify({'detected_objects': [], 'image': ''})


if __name__ == '__main__':
    app.run(debug=True)
