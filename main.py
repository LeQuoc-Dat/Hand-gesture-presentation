import cv2
import mediapipe as mp
import time
from gesture_detection import is_fist_closed, is_hand_open
from powerpoint_control import PowerPointController
from utils import resize_image

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
cap = cv2.VideoCapture(0)

desired_width = 800
desired_height = 600

ppt_controller = PowerPointController(r".\\slide\\demo1.pptx")
previous_x = None
last_gesture_time = time.time()
last_slide_change_time = time.time()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = resize_image(image, desired_width, desired_height)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            current_time = time.time()

            if is_fist_closed(hand_landmarks) and current_time - last_gesture_time > 2:
                ppt_controller.stop_presentation()
                last_gesture_time = current_time

            elif is_hand_open(hand_landmarks) and current_time - last_gesture_time > 2:
                ppt_controller.start_presentation()
                last_gesture_time = current_time

            if ppt_controller.is_active:
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                image_width, image_height = image.shape[1], image.shape[0]
                index_finger_x = int(index_finger_tip.x * image_width)

                if previous_x is not None and current_time - last_slide_change_time > 1:
                    if index_finger_x < previous_x - 50:
                        ppt_controller.previous_slide()
                        last_slide_change_time = current_time
                    elif index_finger_x > previous_x + 50:
                        ppt_controller.next_slide()
                        last_slide_change_time = current_time

                previous_x = index_finger_x

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
ppt_controller.close()
