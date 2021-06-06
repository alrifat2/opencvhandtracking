import cv2
import mediapipe as mp


class HandGesture():
    def __init__(self, mode=False, maxNumHand=2, detectionCon =0.5, trackingCon = 0.5):
        self.mode = mode
        self.maxNumHand = maxNumHand
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxNumHand, self.detectionCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils


    def drawHand(self, img, draw=True):
        rgbIMG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgbIMG)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand, self.mpHands.HAND_CONNECTIONS)
        return img

    def handPosition(self, img, whichHand=0, draw=True):
        landmarkList = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[whichHand]
            for id, landmark in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                landmarkList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (124, 252, 0), cv2.FILLED)

        return landmarkList

