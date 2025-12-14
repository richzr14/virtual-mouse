# 🖱️ Virtual Mouse with Hand Gestures (Python)

A camera-based virtual mouse system that allows users to control the mouse cursor using hand gestures without using any physical mouse.

## 🚀 Features
- Control mouse movement using hand gestures
- Left-click using finger distance gesture
- Real-time hand tracking through webcam
- Smooth cursor movement to reduce shaking
- No external hardware required

## 🛠️ Technologies Used
- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## 🧠 How It Works
1. Webcam captures live video
2. MediaPipe detects hand landmarks and finger positions
3. Hand coordinates are mapped to screen coordinates
4. PyAutoGUI performs mouse actions like movement and click
5. Smoothing logic improves cursor stability

## 🎯 Use Cases
- Touchless computer interaction
- Accessibility solutions
- Computer vision learning project
