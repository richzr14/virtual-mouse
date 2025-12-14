import cv2
import mediapipe as mp
import pyautogui
import math

# Screen size
screen_width, screen_height = pyautogui.size()

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Previous cursor location (for smoothing)
prev_x, prev_y = 0, 0
smoothening = 7

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Index finger tip (landmark 8)
            x1 = int(hand_landmarks.landmark[8].x * w)
            y1 = int(hand_landmarks.landmark[8].y * h)

            # Thumb tip (landmark 4)
            x2 = int(hand_landmarks.landmark[4].x * w)
            y2 = int(hand_landmarks.landmark[4].y * h)

            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Map coordinates
            screen_x = screen_width * x1 / w
            screen_y = screen_height * y1 / h

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)

            prev_x, prev_y = curr_x, curr_y

            # Distance between thumb & index (click gesture)
            distance = math.hypot(x2 - x1, y2 - y1)

            if distance < 40:
                pyautogui.click()
                pyautogui.sleep(0.2)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
