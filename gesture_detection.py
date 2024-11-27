import mediapipe as mp

mp_hands = mp.solutions.hands

def is_fist_closed(hand_landmarks):
    def distance(tip, base):
        return ((tip.x - base.x) ** 2 + (tip.y - base.y) ** 2) ** 0.5

    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    thumb_dist = distance(thumb_tip, wrist)
    index_dist = distance(index_finger_tip, wrist)
    middle_dist = distance(middle_finger_tip, wrist)
    ring_dist = distance(ring_finger_tip, wrist)
    pinky_dist = distance(pinky_tip, wrist)

    return all(d < 0.15 for d in [thumb_dist, index_dist, middle_dist, ring_dist, pinky_dist])


def is_hand_open(hand_landmarks):
    tips = [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    dips = [
        mp_hands.HandLandmark.THUMB_IP,
        mp_hands.HandLandmark.INDEX_FINGER_DIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_DIP,
        mp_hands.HandLandmark.RING_FINGER_DIP,
        mp_hands.HandLandmark.PINKY_DIP
    ]
    open_fingers = 0
    for tip, dip in zip(tips, dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            open_fingers += 1
    return open_fingers == 5
